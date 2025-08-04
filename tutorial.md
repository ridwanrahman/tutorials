# Localstack dynamodb tutorial

This tutorial needs:
1. docker desktop
2. python3.7+ installed
3. basic knowledge of terminal

##  Setting up localstack
```bash
mkdir localstack-tutorial

cd localstack-tutorial
```

### Create docker compose file

```dockerfile
version: '3.8'

services:
  localstack:
    container_name: localstack-main
    image: localstack/localstack:latest
    ports:
      - "4566:4566"            # LocalStack Gateway
      - "4510-4559:4510-4559"  # External services port range (optional)
    environment:
      # LocalStack configuration
      - DEBUG=1
      - SERVICES=dynamodb,s3,lambda,apigateway,sqs,sns
      - DOCKER_HOST=unix:///var/run/docker.sock
      - PERSISTENCE=1
      - DATA_DIR=/tmp/localstack/data
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
    networks:
      - localstack-network

networks:
  localstack-network:
    driver: bridge
```

### Start localstack

```
# Start LocalStack in detached mode
docker-compose up -d

# Check if LocalStack is running
docker-compose ps

# View logs (optional)
docker-compose logs -f localstack
```

### Verify localstack is running

```bash
# Test if LocalStack is responding
curl http://localhost:4566/_localstack/health
# You should see output showing available services
```

### Install AWS CLI

```bash
# Install AWS CLI using pip
pip install awscli

# Or using Homebrew
brew install awscli

# Configure AWS CLI for LocalStack
aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set region us-east-1
aws configure set output json
```



