#!/usr/bin/env bash

cd ~/polo

echo Polo is logging
source bin/activate

raspistill -o ~/Desktop/polo/photos/image.jpg

python3 /home/pi/Desktop/polo/polo.py

echo Polo has logged image
echo Deleting image

rm ~/Desktop/polo/photos/image.jpg

deactivate

cd ~
