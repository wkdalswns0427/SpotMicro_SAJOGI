# 12 servo motors angle test
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
servo = [12]

for i in range(12):
  servo[i] = servo.Servo(pca.channels[i])
# servo0 = servo.Servo(pca.channels[0])
# servo1 = servo.Servo(pca.channels[1])
# servo2 = servo.Servo(pca.channels[2])
# servo3 = servo.Servo(pca.channels[3])
# servo4 = servo.Servo(pca.channels[4])
# servo5 = servo.Servo(pca.channels[5])
# servo6 = servo.Servo(pca.channels[6])
# servo7 = servo.Servo(pca.channels[7])
# servo8 = servo.Servo(pca.channels[8])
# servo9 = servo.Servo(pca.channels[9])
# servo10 = servo.Servo(pca.channels[10])
# servo11 = servo.Servo(pca.channels[11])

print("all servo to 0")
for i in range(12):
  servo[i].angle = 0
time.sleep(10)

print("all servo to 180")
for i in range(12):
  servo[i].angle = 180
time.sleep(10)

print("all servo to 90")
for i in range(12):
  servo[i].angle = 90
time.sleep(10)

pca.deinit()
