# DynamoDB Streams Tutorial

## Purpose
Dynamodb streams captures changes to items in a dynamodb table. when you add, update or delete an item,
the stream captures these changes in real time.

This is useful for:
1. triggering lambda functions
2. replicating data
3. analytics and auditing
4. real-time notifications

## Setup localstack with streams and lambda
```dockerfile
version: '3.8'

services:
  localstack:
    container_name: localstack-streams
    image: localstack/localstack:latest
    ports:
      - "4566:4566"
    environment:
      - DEBUG=1
      - SERVICES=dynamodb,lambda,logs
      - DOCKER_HOST=unix:///var/run/docker.sock
      - PERSISTENCE=1
    volumes:
      - "./volume:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
```