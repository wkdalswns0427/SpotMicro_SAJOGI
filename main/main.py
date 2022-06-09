import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import keyboard

import drivers
import movement as mv

i2c = busio.I2C(SCL, SDA)
display = drivers.Lcd()
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
def main():
    display.lcd_display_string("Hi I am Spot!", 1)
    display.lcd_display_string("Enter command",2)
    try:
        if keyboard.is_pressed('w'):
            mv.move_forward()
        elif keyboard.is_pressed('a'):
            mv.turn_left()
        elif keyboard.is_pressed('d'):
            mv.turn_right()
        elif keyboard.is_pressed('q'):
            mv.return_initial()

    except KeyboardInterrupt:
        display.lcd_clear() 
        display.lcd_display_string("Spotty down", 1)
        print("system interrupted")


if __name__ == '__main__':
    main()