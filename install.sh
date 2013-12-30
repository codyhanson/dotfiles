#!/usr/bin/env bash

#shortcut script to make sure we have what we need
#to run installDotFiles.py

sudo apt-get install python-pip
sudo pip install requests

#now run the actuall installation.
./installDotFiles.py
