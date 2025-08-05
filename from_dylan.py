import boto3
import zipfile
import os

# LocalStack endpoint
ENDPOINT_URL = 'http://localhost:4566'

# Set up Boto3 clients
dynamodb = boto3.client('dynamodb', endpoint_url=ENDPOINT_URL, region_name='ap-southeast-2', aws_access_key_id='dummy',
                        aws_secret_access_key='dummy')
lambda_client = boto3.client('lambda', endpoint_url=ENDPOINT_URL, region_name='ap-southeast-2', aws_access_key_id='dummy',
                             aws_secret_access_key='dummy')


def create_dynamodb_table_with_stream(table_name):
    try:
        # Create a DynamoDB table with a stream
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{'AttributeName': 'key', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5},
            StreamSpecification={'StreamEnabled': True, 'StreamViewType': 'NEW_IMAGE'}
        )
        print(f"Table {table_name} created.")

        # Wait for the table to be active
        dynamodb.get_waiter('table_exists').wait(TableName=table_name)

        # Get the stream ARN
        table_description = dynamodb.describe_table(TableName=table_name)
        stream_arn = table_description['Table']['LatestStreamArn']
        print(f"Stream ARN: {stream_arn}")

        return stream_arn
    except Exception as e:
        print(e)


def create_zip_file(file_name, handler_code):
    with open(file_name, 'w') as f:
        f.write(handler_code)

    zip_file_name = 'lambda_function.zip'
    with zipfile.ZipFile(zip_file_name, 'w') as z:
        z.write(file_name, os.path.basename(file_name))

    os.remove(file_name)
    return zip_file_name


def create_lambda_function(function_name, zip_file_name):
    with open(zip_file_name, 'rb') as f:
        zip_bytes = f.read()

    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.9',
            Role='arn:aws:iam::000000000000:role/lambda-role',
            Handler='lambda_function.lambda_handler',
            Code={'ZipFile': zip_bytes}
        )
        print(f"Lambda function {function_name} created.")
    except Exception as e:
        print(e)


def create_event_source_mapping(function_name, stream_arn):
    try:
        response = lambda_client.create_event_source_mapping(
            EventSourceArn=stream_arn,
            FunctionName=function_name,
            StartingPosition='LATEST'
        )
        print("Event source mapping created:", response['UUID'])
    except Exception as e:
        print(e)


# Example handler code for Lambda function
lambda_handler_code = """
def lambda_handler(event, context):
    print("Received event:", event)
    return "Processed"
"""

# Main execution
table_name = 'MyTable3'
lambda_function_name = 'MyLambdaFunction'

sample_record_from_dynamodb = {
  "key": {
    "S": "LISTING-148032636"
  },
  "transactionId": {
    "S": "73a41c32-76d1-4512-ac42-326dbc552709"
  },
  "auditMessage": {
    "S": "Unused unit version for a sale, https://rea-group.slack.com/archives/C02CGQ2R5L1/p1749716429854199"
  },
  "matchDateTime": {
    "S": "2025-06-17T10:27:57"
  },
  "operation": {
    "M": {
      "cleansedAddress": {
        "S": "18 Bayswater Avenue, Tallawong, NSW 2762"
      },
      "propertyId": {
        "S": "20166689"
      },
      "type": {
        "S": "unmatch"
      }
    }
  },
  "requesterEmail": {
    "S": "danny.renato@proptrack.com"
  },
  "target": {
    "M": {
      "targetAddress": {
        "S": "18 Bayswater Avenue, Tallawong, NSW 2762"
      },
      "targetId": {
        "S": "148032636"
      },
      "targetType": {
        "S": "LISTING"
      }
    }
  },
  "ticketId": {
    "S": "N/A"
  }
}

stream_arn = create_dynamodb_table_with_stream(table_name)
zip_file_name = create_zip_file('lambda_function.py', lambda_handler_code)
create_lambda_function(lambda_function_name, zip_file_name)
create_event_source_mapping(lambda_function_name, stream_arn)


# write to dynamo table
dynamodb.put_item(
    TableName=table_name,
    Item={'id': {'S': '123'}}
)

