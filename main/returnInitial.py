# set all servos to initial position
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

# for i in range(8):
#     servo[i] = servo.Servo(pca.channels[i])
servo0 = servo.Servo(pca.channels[0])
servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[4])
servo5 = servo.Servo(pca.channels[5])
servo6 = servo.Servo(pca.channels[6])
servo7 = servo.Servo(pca.channels[7])

# for i in range(8):
#     servo[i].angle = 90
#     time.sleep(0.01)

servo0.angle = 90
servo1.angle = 90
servo2.angle = 90
servo3.angle = 90
servo4.angle = 90
servo5.angle = 90
servo6.angle = 90
servo7.angle = 90

pca.deinit()
