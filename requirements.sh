#!/bin/sh

echo "check your pi enabled i2c driver"
echo "you run this only once if initial, enter 0 else 1"

read num
echo "is this first time? : $num"
if [ $num -eq 0 ] ; then
    sudo pip3 install pyautogui
    sudo pip3 install keyboard
    sudo pip3 install adafruit-circuitpython-pca9685
    sudo pip3 install pybullet
    git clone https://github.com/the-raspberry-pi-guy/lcd.git
    bash ./lcd/setup.sh
fi

if [ $num -eq 1 ] ; then
    echo "bye"
fi
