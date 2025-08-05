import json


def lambda_handler(event, context):
    """Minimal Lambda function"""

    print(f"Lambda triggered! Event: {json.dumps(event)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambdaasdfasdfadsf!')
    }