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
servo3 = servo.Servo(pca1.channels[3])
servo4 = servo.Servo(pca1.channels[4])
servo5 = servo.Servo(pca1.channels[5])
servo6 = servo.Servo(pca1.channels[6])
servo7 = servo.Servo(pca1.channels[7])
servo8 = servo.Servo(pca1.channels[8])
servo9 = servo.Servo(pca1.channels[9])
servo10 = servo.Servo(pca1.channels[10])
servo11 = servo.Servo(pca1.channels[11])

# standard standing position

display.lcd_display_string("   O        O   ", 1)  # Write line of text to first line of display
display.lcd_display_string("    \______/    ", 2)
time.sleep(2)
display.lcd_clear() 
time.sleep(0.1)
display.lcd_display_string("   back to init   ", 1) 

servo0.angle = 90
servo1.angle = 80
servo2.angle = 90
servo3.angle = 100
servo4.angle = 90
servo5.angle = 90
servo6.angle = 100
servo7.angle = 90
servo8.angle = 90
servo9.angle = 90
servo10.angle = 80
servo11.angle = 80

pca1.deinit()
