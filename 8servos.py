# 8 servos test with pca9685

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)

pca.frequency = 50

servo0 = servo.Servo(pca.channels[0])
servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[4])
servo5 = servo.Servo(pca.channels[5])
servo6 = servo.Servo(pca.channels[6])
servo7 = servo.Servo(pca.channels[7])

# We sleep in the loops to give the servo time to move into position.
for i in range(180):
    servo0.angle = i
    servo1.angle = i
    servo2.angle = i
    servo3.angle = i
    servo4.angle = i
    servo5.angle = i
    servo6.angle = i
    servo7.angle = i
    time.sleep(0.03)
for i in range(180):
    servo0.angle = 180 - i
    servo1.angle = 180 - i
    servo2.angle = 180 - i
    servo3.angle = 180 - i
    servo4.angle = 180 - i
    servo5.angle = 180 - i
    servo6.angle = 180 - i
    servo7.angle = 180 - i
    time.sleep(0.03)

# You can also specify the movement fractionally.
fraction = 0.0
while fraction < 1.0:
    servo0.fraction = fraction
    servo1.fraction = fraction
    servo2.fraction = fraction
    servo3.fraction = fraction
    servo4.fraction = fraction
    servo5.fraction = fraction
    servo6.fraction = fraction
    servo7.fraction = fraction
    fraction += 0.01
    time.sleep(0.03)

pca.deinit()