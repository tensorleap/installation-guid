# Tensorleap Installation on EC2 Instance with GPU

This guide provides instructions for deploying an EC2 instance using a CloudFormation stack and installing Tensorleap on an Ubuntu system equipped with an NVIDIA GPU.

## Step 1: Deploy CloudFormation Stack

To deploy the CloudFormation stack, you need to run the following command after authenticating to your dev account. This step should be performed only once, and when not in use, the stack should be deleted.

### Ensure You're Using the Correct Account

Make sure you're authenticated with the dev account (account id: 898022457080).

```bash
CFN_STACK_NAME="tensorleap-ec2"
aws cloudformation deploy --stack-name $CFN_STACK_NAME --template-file developers-ec2-infra.yaml --capabilities CAPABILITY_NAMED_IAM
```

### Obtain CloudFormation Outputs

Once the stack is deployed, retrieve the necessary outputs to create the EC2 instance:

```bash
SubnetID=$(aws cloudformation describe-stacks --stack-name $CFN_STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='SubnetID'].OutputValue" --output text)

AmiID=$(aws cloudformation describe-stacks --stack-name $CFN_STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='AmiID'].OutputValue" --output text)

EC2InstanceProfile=$(aws cloudformation describe-stacks --stack-name $CFN_STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='EC2InstanceProfile'].OutputValue" --output text)
```

## Step 2: Create EC2 Instance

Edit the following parameters as needed:
- `InstanceType`: Choose an instance type suitable for your workload (default is `g6.xlarge`).
- `InstanceName`: Assign a name to the instance (default is `tensorleap-dev-gpu-ec2`).

Then run the command:

```bash
InstanceType="g6.xlarge"
InstanceName="tensorleap-dev-gpu-ec2"
aws ec2 run-instances \
    --image-id $AmiID \
    --instance-type $InstanceType \
    --subnet-id $SubnetID \
    --iam-instance-profile Name=$EC2InstanceProfile \
    --block-device-mappings '[{"DeviceName":"/dev/xvda","Ebs":{"VolumeSize":100,"VolumeType":"gp3"}}]' \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$InstanceName}]"
```

## Step 3: Connect to the EC2 Instance

### Install SSM Session Manager Plugin

Install the SSM Session Manager Plugin following the instructions from AWS:
[Session Manager Plugin Installation](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)

### Connect to the EC2 Instance

```bash
aws ssm start-session --target <instance-id>
```

## Step 4: Install Docker and Tensorleap

### Install Docker

Add your user to the Docker group and set up Docker:

```bash
sudo usermod -aG docker $(whoami)
newgrp docker
docker ps
```

### Install Tensorleap

Use the following command to install Tensorleap:

```bash
curl -s https://raw.githubusercontent.com/tensorleap/leap-cli/master/install.sh | bash
leap server install
```

## Step 5: Port Forwarding

To connect to Tensorleap, use the following port forwarding command:

```bash
aws ssm start-session --target <instance-id> --document-name AWS-StartPortForwardingSession --parameters '{"portNumber":["4589"],"localPortNumber":["4589"]}'
```

## Step 6: Terminate the EC2 Instance

When finished, terminate the EC2 instance with this command:

```bash
aws ec2 terminate-instances --instance-ids <instance-id>
```

