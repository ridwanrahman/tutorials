import boto3

lambda_client = boto3.client('lambda',
                             region_name='ap-southeast-2',
                             endpoint_url='http://localhost:4566',
                             aws_access_key_id='test',
                             aws_secret_access_key='test')
dynamodb_client = boto3.client('dynamodb',
                             region_name='ap-southeast-2',
                             endpoint_url='http://localhost:4566',
                             aws_access_key_id='test',
                             aws_secret_access_key='test')
dynamodbstreams_client = boto3.client('dynamodbstreams', region_name='ap-southeast-2', endpoint_url='http://localhost:4566',aws_access_key_id='test',aws_secret_access_key='test')
table_name = 'MyStreamEnabledTable'

response = dynamodb_client.delete_table(TableName=table_name)
print(f"Table {table_name} deletion initiated.")

# Wait until the table is deleted
dynamodb_client.get_waiter('table_not_exists').wait(TableName=table_name)
print(f"Table {table_name} successfully deleted.")