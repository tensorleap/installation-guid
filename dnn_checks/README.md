# GPU Health Checker for Deep Neural Network (DNN) Packages
This repository contains a Python script to check if your GPU is properly configured and operational for running deep neural network (DNN) packages.
This is useful for ensuring that your GPU is being utilized effectively.

Requirements
Python 3.8
NVIDIA GPU with CUDA support
CUDA Toolkit installed (compatible with your GPU)
NVIDIA drivers installed
Poetry installed

## Installing Poetry
Poetry is a tool for dependency management and packaging in Python.
It allows us to declare the libraries we depend on, and it will manage (install/update) them for you. 
To install Poetry, please refer to the official documentation for installing Poetry on your system:
https://python-poetry.org/docs/#installation

## Installing dependencies
To install the dependencies for this project, run the following command:
```bash
poetry install
```

## Running the GPU Health Checker
To run the GPU Health Checker, use the following command:
```bash
make check_tf_gpu
```

This will run the GPU Health Checker script and display the results in your terminal.

## Running the GPU Health Checker on docker
To run the GPU Health Checker inside dockerized environment, first pull the docker image from the public ECR repository and then run the docker container using the following commands:
```bash
docker pull public.ecr.aws/tensorleap/gpu_checks:latest
```

```bash
docker run  public.ecr.aws/tensorleap/gpu_checks:latest
```