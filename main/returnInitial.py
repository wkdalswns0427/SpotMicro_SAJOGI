# set all servos to initial position
import time

from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca1 = PCA9685(i2c)

pca1.frequency = 50

# for i in range(8):
#     servo[i] = servo.Servo(pca.channels[i])
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

# for i in range(8):
#     servo[i].angle = 90
#     time.sleep(0.01)

servo0.angle = 25
servo1.angle = 40
servo2.angle = 90
servo3.angle = 150
servo4.angle = 140
servo5.angle = 90
servo6.angle = 60
servo7.angle = 40
servo8.angle = 90
servo9.angle = 130
servo10.angle = 140
servo11.angle = 90

pca1.deinit()
