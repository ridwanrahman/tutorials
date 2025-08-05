import boto3
import json
import time
from datetime import datetime, timedelta
from decimal import Decimal

# Configure DynamoDB client
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='ap-southeast-2'
)

table = dynamodb.Table('user_activity')


def create_timestamp(minutes_ago=0):
    """Create timestamp string"""
    dt = datetime.utcnow() - timedelta(minutes=minutes_ago)
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def simulate_user_login(user_id):
    """Simulate user login"""
    print(f"🔑 Simulating login for user {user_id}")

    table.put_item(
        Item={
            'user_id': user_id,
            'timestamp': create_timestamp(),
            'activity_type': 'login',
            'ip_address': '192.168.1.100',
            'device': 'web',
            'session_id': f'sess_{user_id}_{int(time.time())}'
        }
    )
    print(f"✅ Login recorded for {user_id}")


def simulate_user_purchase(user_id, amount, product):
    """Simulate user purchase"""
    print(f"💳 Simulating purchase for user {user_id}: {product} - ${amount}")

    table.put_item(
        Item={
            'user_id': user_id,
            'timestamp': create_timestamp(),
            'activity_type': 'purchase',
            'amount': Decimal(str(amount)),
            'product': product,
            'transaction_id': f'txn_{user_id}_{int(time.time())}'
        }
    )
    print(f"✅ Purchase recorded for {user_id}")


def simulate_user_logout(user_id):
    """Simulate user logout"""
    print(f"🚪 Simulating logout for user {user_id}")

    table.put_item(
        Item={
            'user_id': user_id,
            'timestamp': create_timestamp(),
            'activity_type': 'logout',
            'session_duration_minutes': 45
        }
    )
    print(f"✅ Logout recorded for {user_id}")


def update_user_activity(user_id, timestamp, new_device):
    """Update existing activity"""
    print(f"🔄 Updating activity for user {user_id}")

    table.update_item(
        Key={
            'user_id': user_id,
            'timestamp': timestamp
        },
        UpdateExpression='SET device = :device, updated_at = :updated',
        ExpressionAttributeValues={
            ':device': new_device,
            ':updated': create_timestamp()
        }
    )
    print(f"✅ Activity updated for {user_id}")


def delete_user_activity(user_id, timestamp):
    """Delete user activity"""
    print(f"🗑️ Deleting activity for user {user_id}")

    table.delete_item(
        Key={
            'user_id': user_id,
            'timestamp': timestamp
        }
    )
    print(f"✅ Activity deleted for {user_id}")


def run_user_activity_simulation():
    """Run complete user activity simulation"""
    print("🚀 Starting User Activity Simulation")
    print("=" * 50)

    users = ['alice', 'bob', 'charlie']

    # Simulate user journeys
    for user in users:
        print(f"\n👤 User Journey for: {user}")
        print("-" * 30)

        # 1. User logs in
        simulate_user_login(user)
        time.sleep(2)  # Wait for stream processing

        # 2. User makes a purchase
        products = ['Laptop', 'Headphones', 'Keyboard']
        amounts = [999.99, 199.99, 89.99]

        for i, user_id in enumerate([user]):
            product = products[i % len(products)]
            amount = amounts[i % len(amounts)]
            simulate_user_purchase(user, amount, product)
            time.sleep(2)

        # 3. User logs out
        simulate_user_logout(user)
        time.sleep(2)

    # Wait a bit, then demonstrate updates and deletes
    print(f"\n🔄 Demonstrating Updates and Deletes")
    print("-" * 40)

    # Get some activity to update/delete
    time.sleep(3)

    # Update activity (change device)
    response = table.scan(Limit=1)
    if response['Items']:
        item = response['Items'][0]
        update_user_activity(item['user_id'], item['timestamp'], 'mobile')
        time.sleep(2)

        # Delete the same activity
        delete_user_activity(item['user_id'], item['timestamp'])
        time.sleep(2)

    print(f"\n🎉 Simulation Complete!")
    print("Check LocalStack logs to see Lambda processing:")
    print("docker-compose logs -f localstack | grep -i lambda")


if __name__ == "__main__":
    try:
        run_user_activity_simulation()
    except Exception as e:
        print(f"❌ Error during simulation: {e}")
        import traceback

        traceback.print_exc()