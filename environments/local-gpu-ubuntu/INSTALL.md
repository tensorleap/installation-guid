# Installation Guide for Tensorleap on Ubuntu with GPU

This guide provides detailed instructions for installing Tensorleap on a standalone Ubuntu system equipped with an NVIDIA GPU. Follow these steps to ensure a successful setup.

## Prerequisites

Before beginning the installation, make sure you meet the following requirements:
- Ubuntu 20.04 or higher.
- NVIDIA GPU
- Administrative privileges on your system.

### Install nvidia
```bash
sudo apt-get update
sudo apt-get install nvidia-driver-535
sudo reboot
```

### install cuda
```bash
sudo apt-get update
sudo apt-get install cuda
```
<details>
  <summary>If you get: `E: Unable to locate package cuda`</summary>

  ```bash
  wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
  sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
  sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
  sudo add-apt-repository "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
  sudo apt-get update
  sudo apt-get install cuda
  ```
</details>

### install docker and docker nvidia2
```bash
sudo apt  install docker.Io
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker
```

### check drivers
```bash
sudo docker run --rm --gpus all nvidia/cuda:12.4.1-devel-ubuntu20.04 nvidia-smi
sudo docker run --rm --gpus all public.ecr.aws/tensorleap/gpu_checks:latest
```

### install tensorleap
```bash
curl -s https://raw.githubusercontent.com/tensorleap/leap-cli/master/install.sh | bash
leap server install
```
