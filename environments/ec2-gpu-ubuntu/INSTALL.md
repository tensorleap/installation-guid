# Installation Guide for Tensorleap on Amazon EC2 with GPU

This guide will help you deploy Tensorleap on an Amazon EC2 instance equipped with an NVIDIA GPU, allowing you to leverage cloud computing to scale your machine learning tasks.

## Prerequisites

Before you begin, ensure you have the following:
- An AWS account.
- Basic knowledge of AWS services.
- SSH access to your EC2 instance.


## Instance Requirements

Make sure your EC2 instance meets these specifications:
- **Memory**: More than 16 GB of RAM.
- **Storage**: At least 100 GB of available storage.

## Step 1: Launch an EC2 Instance
<details>
  <summary>Use aws cli</summary>
# Creating an EC2 Instance with GPU via AWS CLI

  This guide provides a quick walkthrough to set up an Amazon EC2 instance with GPU support using the AWS CLI.

## Prerequisites
  - AWS CLI installed and configured with your AWS credentials.

## Steps

### Create a Key Pair
  Generate a key pair for SSH access:
  ```bash
  aws ec2 create-key-pair --key-name MyGPUKey --query 'KeyMaterial' --output text > MyGPUKey.pem
  chmod 400 MyGPUKey.pem
  ```
### Create a Security Group
Create and configure a security group to allow SSH:

  ```bash
  aws ec2 create-security-group --group-name GPUSecurityGroup --description "GPU Instance Security Group"
  aws ec2 authorize-security-group-ingress --group-id {Security_Group_ID} --protocol tcp --port 22 --cidr 0.0.0.0/0
  ```
  Replace {Security_Group_ID} with the actual security group ID returned from the create command.
### Launch the Instance
  Launch your EC2 instance:

  ```bash
  AMI_ID=ami-0cd59ecaf368e5ccf # select ubuntu 20.04
  aws ec2 run-instances --image-id $AMI_ID --count 1 --instance-type g4dn.xlarge --key-name MyGPUKey --security-group-ids {Security_Group_ID} --block-device-mappings DeviceName=/dev/sda1,Ebs={VolumeSize=100}
  ```
  Replace {Security_Group_ID} with your security group ID.
### Connect to Your Instance
  Connect to your instance via SSH:
  ```bash
  ssh -i "MyGPUKey.pem" ubuntu@{Public_DNS}
  ```
  Replace {Public_DNS} with the public DNS of your EC2 instance, which you can find in the AWS Management Console or via CLI queries.

</details>

<details>
  <summary>Use EC2 user interface</summary>
# Creating an EC2 Instance with GPU on Ubuntu 20.04 via AWS Management Console

This guide provides step-by-step instructions for setting up an Amazon EC2 instance with GPU capabilities using Ubuntu 20.04, ideal for tasks requiring high computational power such as machine learning or intensive data processing.

## Prerequisites
- You have an AWS account and are logged into the AWS Management Console.

## Steps

### 1. Choose an AMI
1. Navigate to the **EC2 Dashboard**.
2. Click on **Launch Instance**.
3. Select the **AWS Marketplace** tab, then search for and select "Ubuntu 20.04".
4. Choose an AMI that supports GPUs, such as the "Deep Learning AMI (Ubuntu 20.04) Version".

### 2. Choose an Instance Type
1. After selecting the AMI, proceed to choose an instance type.
2. Filter the options by GPU instances to find one that fits your needs, such as `g4dn.xlarge`.

### 3. Configure Instance
1. Click on **Configure Instance Details**.
2. Set the number of instances, network, and other configurations as needed.
3. Optionally, enable **Auto-assign Public IP** to ensure your instance is accessible over the internet.

### 4. Add Storage
1. Click on **Add Storage**.
2. Adjust the size and type of storage according to your requirements. For GPU tasks, consider increasing the size to accommodate large datasets or tools.

### 5. Configure Security Group
1. Navigate to **Configure Security Group**.
2. You can create a new security group or select an existing one.
3. Ensure you add a rule that allows SSH traffic (port 22) from your IP address or from anywhere (0.0.0.0/0), though the latter is less secure.

### 6. Review and Launch
1. Review all settings.
2. Click on **Launch**.
3. You will be prompted to select a key pair. If you do not have one, create a new key pair. Download it and keep it safe, as it will be needed to SSH into the instance.

### 7. Connect to Your Instance
1. Once the instance is running, navigate to your EC2 Dashboard.
2. Find your new instance and note the **Public DNS (IPv4)**.
3. Connect via SSH using the downloaded key pair:
   ```bash
   ssh -i "path_to_your_key_pair.pem" ubuntu@your_instance_public_dns
	```

</details>


