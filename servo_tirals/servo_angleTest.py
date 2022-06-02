# 12 servo motors angle test
import time
from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

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

print("all servo to 0")
servo0.angle = 0
servo1.angle = 0
servo2.angle = 0
servo3.angle = 0
servo4.angle = 0
servo5.angle = 0
servo6.angle = 0
servo7.angle = 0
servo8.angle = 0
servo9.angle = 0
servo10.angle = 0
servo11.angle = 0
time.sleep(5)

print("all servo to 180")
servo0.angle = 180
servo1.angle = 180
servo2.angle = 180
servo3.angle = 180
servo4.angle = 180
servo5.angle = 180
servo6.angle = 180
servo7.angle = 180
servo8.angle = 180
servo9.angle = 180
servo10.angle = 180
servo11.angle = 180
time.sleep(5)

print("all servo to 90")
servo0.angle = 90
servo1.angle = 90
servo2.angle = 90
servo3.angle = 90
servo4.angle = 90
servo5.angle = 90
servo6.angle = 90
servo7.angle = 90
servo8.angle = 90
servo9.angle = 90
servo10.angle = 90
servo11.angle = 90
time.sleep(5)

print("terminate")
pca1.deinit()
