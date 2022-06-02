import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

import movement as mv

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c, address=0x40)

pca1.frequency = 50

servo0 = servo.Servo(pca1.channels[0])
servo1 = servo.Servo(pca1.channels[1])
servo2 = servo.Servo(pca1.channels[2])
servo3 = servo.Servo(pca1.channels[3])
servo4 = servo.Servo(pca1.channels[4])
servo5 = servo.Servo(pca1.channels[5])
servo6 = servo.Servo(pca1.channels[6])
servo7 = servo.Servo(pca1.channels[7])
servo8 = servo.Servo(pca1.channels[8])
servo9 = servo.Servo(pca1.channels[9])
servo10 = servo.Servo(pca1.channels[10])
servo11 = servo.Servo(pca1.channels[11])

# forward movement
mv.move_forward()
mv.return_initial()
# not made yet
mv.move_backward()
mv.crawl()
