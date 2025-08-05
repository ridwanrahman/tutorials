import time
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
        response = dynamodb.delete_table(TableName=table_name)
        print(f"Table {table_name} deletion initiated.")
        # Wait for the table to be active
        dynamodb.get_waiter('table_not_exists').wait(TableName=table_name)
    except Exception as e:
        print(e)

    try:
        # Create a DynamoDB table with a stream
        table_definition = {
            'TableName': table_name,
            'AttributeDefinitions': [
                {'AttributeName': 'key', 'AttributeType': 'S'},
                {'AttributeName': 'transactionId', 'AttributeType': 'S'}
            ],
            'KeySchema': [
                {'AttributeName': 'key', 'KeyType': 'HASH'},
                {'AttributeName': 'transactionId', 'KeyType': 'RANGE'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            },
            'StreamSpecification': {'StreamEnabled': True, 'StreamViewType': 'NEW_IMAGE'}
        }

        response = dynamodb.create_table(**table_definition)
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

def insert_data(record, table_name):
    try:
        response = dynamodb.put_item(
            TableName=table_name,
            Item=record
        )
        print(f"Data inserted: {response}")
        return response
    except Exception as e:
        print(f"Error inserting data: {e}")
        return None

def create_zip_file():
    zip_file_name = 'lambda_function.zip'
    file_name = 'lambda_handler.py'
    with zipfile.ZipFile(zip_file_name, 'w') as z:
        z.write(file_name, os.path.basename(file_name))

    # os.remove(file_name)
    return zip_file_name

def create_lambda_function(function_name, zip_file_name):
    with open(zip_file_name, 'rb') as f:
        zip_bytes = f.read()

    try:
        delete_response = lambda_client.delete_function(FunctionName=function_name)
        time.sleep(5)
    except Exception as e:
        print(e)

    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.9',
            Role='arn:aws:iam::000000000000:role/lambda-role',
            Handler='lambda_handler.lambda_handler',
            Code={'ZipFile': zip_bytes}
        )
        print(response)
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
        print(response)
        print("Event source mapping created:", response['UUID'])

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # Example handler code for Lambda function

    table_name = 'MyTable4'
    lambda_function_name = 'manual_match_handler'

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
    if stream_arn is None:
        raise Exception("STRAM ARN is None")
    zip_file_name = create_zip_file()
    create_lambda_function(lambda_function_name, zip_file_name)
    create_event_source_mapping(lambda_function_name, stream_arn)

    insert_response = insert_data(sample_record_from_dynamodb, table_name)

