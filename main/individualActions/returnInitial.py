# set all servos to initial position
import time

from board import SCL, SDA
import busio
import drivers
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 50
display = drivers.Lcd()

servo0 = servo.Servo(pca1.channels[0])
servo1 = servo.Servo(pca1.channels[1])
servo2 = servo.Servo(pca1.channels[2])
servo4 = servo.Servo(pca1.channels[4])
servo5 = servo.Servo(pca1.channels[5])
servo6 = servo.Servo(pca1.channels[6])
servo8 = servo.Servo(pca1.channels[8])
servo9 = servo.Servo(pca1.channels[9])
servo10 = servo.Servo(pca1.channels[10])
servo12= servo.Servo(pca1.channels[12])
servo13 = servo.Servo(pca1.channels[13])
servo14 = servo.Servo(pca1.channels[14])

# standard standing position

display.lcd_display_string("   O        O   ", 1)  # Write line of text to first line of display
display.lcd_display_string("    \______/    ", 2)
time.sleep(2)
display.lcd_clear() 
time.sleep(0.1)
display.lcd_display_string("   back to init   ", 1) 

servo0.angle = 80
servo1.angle = 80
servo2.angle = 90
servo4.angle = 110
servo5.angle = 100
servo6.angle = 90
servo8.angle = 90
servo9.angle = 100
servo10.angle = 85
servo12.angle = 90
servo13.angle = 65
servo14.angle = 83

pca1.deinit()

