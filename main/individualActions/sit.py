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

def returnInit():
    servo0.angle = 90
    servo1.angle = 80
    servo2.angle = 100
    servo3.angle = 90
    servo4.angle = 100
    servo5.angle = 100
    servo6.angle = 90
    servo7.angle = 90
    servo8.angle = 80
    servo9.angle = 90
    servo10.angle = 90
    servo11.angle = 80

def sit_one():
    servo3.angle = 60
    servo9.angle = 120
    time.sleep(0.3)
    servo0.angle = 50
    servo6.angle = 130
    time.sleep(0.3)
    servo4.angle = 65
    servo10.angle = 115
    time.sleep(0.3)


def sit_two():
    servo4.angle = 65
    servo10.angle = 115
    servo0.angle = 125
    servo6.angle = 55
    time.sleep(0.2)
    servo1.angle = 115
    servo7.angle = 65
    servo3.angle = 65
    servo9.angle = 115
    time.sleep(0.3)

returnInit()
sit_two()

