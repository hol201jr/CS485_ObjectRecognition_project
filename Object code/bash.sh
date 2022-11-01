#!/bin/bash
#put the following commands into your terminal in order to 
# install the dependacies for the project. If you have any issues
# installing just make a Linux VM and install them there make sure
# that you have a python 3.7 or 3.8 as imageAI is not compatible with 
# python 3.10 as of yet.  
bash -c "command"

# installing OpenCV  
$ pip install opencv-python  
  
  #Note tensorflow may give you issues if you dont have longpath 
  #enabled on windows 10 in order to enable input the following
  # in powershell as admin.

  New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
-Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force

# installing TensorFlow  
$ pip install tensorflow  
  
# installing Keras  
$ pip install keras  
  
# installing ImageAI  
$ pip install imageAI  