#!/usr/bin/env bash

cd ~/polo

echo Polo is logging
source bin/activate

raspistill -o ~/polo/photos/image.jpg

python3 /home/pi/polo/polo.py

echo Polo has logged image
echo Deleting image

rm ~/polo/photos/image.jpg

deactivate

cd ~
