
# Environment Cleanup Guide

This guide provides instructions on how to uninstall NVIDIA drivers, CUDA, and `nvidia-docker2` from an Ubuntu system.

## Uninstalling NVIDIA Drivers

1. List installed NVIDIA drivers:
   ```
   dpkg -l | grep nvidia
   ```
2. Remove NVIDIA drivers:
   ```
   sudo apt-get remove --purge '^nvidia-.*'
   ```
3. Reboot the system:
   ```
   sudo reboot
   ```

## Uninstalling CUDA

1. List installed CUDA packages:
   ```
   dpkg -l | grep cuda
   ```
2. Remove CUDA packages:
   ```
   sudo apt-get --purge remove "cuda*" "nvidia-cuda*"
   ```
3. Clean up the system:
   ```
   sudo apt-get autoremove
   ```
4. Remove the CUDA toolkit directory (if installed manually):
   ```
   sudo rm -rf /usr/local/cuda-<version>
   ```

## Uninstalling NVIDIA Docker Plugin (`nvidia-docker2`)

1. Uninstall `nvidia-docker2`:
   ```
   sudo apt-get purge nvidia-docker2
   ```
2. Clean up the system:
   ```
   sudo apt-get autoremove
   ```
3. Reload the Docker daemon:
   ```
   sudo systemctl restart docker
   ```
