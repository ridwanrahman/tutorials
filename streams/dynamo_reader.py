import json
import boto3


def lambda_handler(event, context):
    """Lambda function that reads from DynamoDB"""

    print("Lambda function started")

    # Create DynamoDB client
    dynamodb = boto3.client(
        'dynamodb',
        endpoint_url='http://localhost:4566',
        region_name='ap-southeast-2',
    )

    try:
        # Scan DynamoDB table
        response = dynamodb.scan(TableName='test-table')
        items = response.get('Items', [])
        print(f"{items=}")

        print(f"Found {len(items)} items in DynamoDB")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Found {len(items)} items',
                'items': items
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }