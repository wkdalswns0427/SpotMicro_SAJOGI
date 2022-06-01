import time
from board import SCL, SDA
import busio
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
#-------------------------------------
#          <front>
# (0 1 2)          (9 10 11)
# 
#
# (6 7 8)          (3 4 5)
#          <hind>
# motor configuration 
#-------------------------------------

# forward movement
def move_forward():
  try:
    servo0.angle = 55
    servo1.angle = 70
    servo2.angle = 70  
    servo1.angle = 90
    servo2.angle = 90  
    
    servo3.angle = 55
    servo4.angle = 70
    servo5.angle = 70 
    servo4.angle = 90
    servo5.angle = 90 
    
    time.sleep(10)
    
    servo6.angle = 55
    servo7.angle = 70
    servo8.angle = 70  
    servo7.angle = 90
    servo8.angle = 90  
  
    servo9.angle = 55
    servo10.angle = 70
    servo11.angle = 70   
    servo10.angle = 90
    servo11.angle = 90  
    
    time.sleep(10)
    
  except KeyboardInterrupt
    print("exit all motion")
 
  
  
