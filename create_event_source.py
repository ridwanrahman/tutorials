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


response = lambda_client.create_event_source_mapping(
    EventSourceArn='arn:aws:dynamodb:ap-southeast-2:000000000000:table/MyStreamEnabledTable/stream/2025-08-05T00:49:48.737',
    FunctionName='arn:aws:lambda:ap-southeast-2:000000000000:function:myLambdaFunction',
    StartingPosition='TRIM_HORIZON',
    BatchSize=100,
    Enabled=True
)
print(response)