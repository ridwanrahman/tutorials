# Cloudformation

## What is cloudformation?
it is a declarative way to outline AWS infrastructure. 

For example withint a clouformation template you say:
1. i want a security group
2. i want 2 ec2 instances using this security group
3. i want two elastic ips for these ec2 instances

Cloudformation will create these for you in the right order, with the exact configuration you specified.

This is called INFRASTRUCTURE AS CODE (IAC)