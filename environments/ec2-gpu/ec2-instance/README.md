# Running CloudFormation Stack
To run the CloudFormation stack, you need to run the following command after authenticating to dev account:
This should be run once - and when not in use, the stack should be deleted.

### Make sure you are using the dev account - account id: 898022457080

```bash
CFN_STACK_NAME="tensorleap-ec2"
aws cloudformation deploy --stack-name $CFN_STACK_NAME --template-file developers-ec2-infra.yaml --capabilities CAPABILITY_NAMED_IAM
```

To create the EC2 Instance - we will need the outputs from above.

```bash
SubnetID=$(aws cloudformation describe-stacks --stack-name $CFN_STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='SubnetID'].OutputValue" --output text)

AmiID=$(aws cloudformation describe-stacks --stack-name $CFN_STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='AmiID'].OutputValue" --output text)

EC2InstanceProfile=$(aws cloudformation describe-stacks --stack-name $CFN_STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='EC2InstanceProfile'].OutputValue" --output text)
```

## Deploy EC2 Instance

Edit `InstanceType` and `InstanceName` \
Run the following command:

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

# Connect to the EC2

1. Install SSM Session Manager Plugin: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html

2. Connect to the EC2 using the following command:

```bash
aws ssm start-session --target <instance-id>
```

# Terminate the EC2

```bash
aws ec2 terminate-instances --instance-ids <instance-id>
```
