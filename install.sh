#!/bin/bash

echo "Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing Python3 and pip..."
sudo apt-get install python3 python3-pip -y

echo "Installing required Python libraries..."
pip3 install socket
pip3 install threading

echo "Setup complete. Ready to run DDoS script."
