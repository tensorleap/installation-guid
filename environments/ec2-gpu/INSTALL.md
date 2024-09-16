# Installation Guide for Tensorleap on Ubuntu with GPU

This guide provides detailed instructions for installing Tensorleap on a standalone Ubuntu system equipped with an NVIDIA GPU. Follow these steps to ensure a successful setup.

## Create ec2 instance
Use the guide environments/ec2-gpu/ec2-instance/README.md

## Prerequisites

Before beginning the installation, make sure you meet the following requirements:
- Ubuntu 20.04 or higher.
- NVIDIA GPU
- Administrative privileges on your system.
- ec2 instance

### Create ec2 instance
Use the guide environments/ec2-gpu/ec2-instance/README.md

### Connet using ssm
```bash
aws ssm start-session --target <instance-id>
```

### Install Docker
```bash
sudo usermod -aG docker $(whoami)
docker ps
newgrp docker
```


### Install Tensorleap
```bash
curl -s https://raw.githubusercontent.com/tensorleap/leap-cli/master/install.sh | bash
leap server install
```

### Connect
```bash
ssm start-session --target <instance-id> --document-name AWS-StartPortForwardingSession --parameters '{"portNumber":["4589"],"localPortNumber":["4589"]}'
```
