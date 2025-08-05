import boto3

lambda_client = boto3.client('lambda',
                             region_name='ap-southeast-2',
                             endpoint_url='http://localhost:4566',
                             aws_access_key_id='test',
                             aws_secret_access_key='test')
dynamo_client = boto3.client('dynamodb',
                             region_name='ap-southeast-2',
                             endpoint_url='http://localhost:4566',
                             aws_access_key_id='test',
                             aws_secret_access_key='test')
dynamodbstreams_client = boto3.client('dynamodbstreams', region_name='ap-southeast-2', endpoint_url='http://localhost:4566',aws_access_key_id='test',aws_secret_access_key='test')


try:
    table = dynamo_client.describe_table(TableName='MyStreamEnabledTable')
    print(table)
except dynamo_client.exceptions.ResourceNotFoundException:
    print("Table does not exist, creating a new one.")


print("asdfasdf")

response = dynamo_client.create_table(
    TableName='MyStreamEnabledTable',
    KeySchema=[
        {
            'AttributeName': 'PK',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'SK',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'PK',
            'AttributeType': 'S'  # String
        },
        {
            'AttributeName': 'SK',
            'AttributeType': 'S'  # String
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
)
# update_table_response = dynamo_client.update_table(
#     TableName='MyStreamEnabledTable',
#     StreamSpecification={
#         'StreamEnabled': True,
#         'StreamViewType': 'NEW_AND_OLD_IMAGES'  # Options: KEYS_ONLY | NEW_IMAGE | OLD_IMAGE | NEW_AND_OLD_IMAGES
#     }
# )

streams = dynamo_client.describe_table(TableName='MyStreamEnabledTable')
stream_arn = streams['Table']['LatestStreamArn']
print(f"Stream ARN: {stream_arn}")
