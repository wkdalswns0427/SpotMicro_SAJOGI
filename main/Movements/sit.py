import time
from board import SCL, SDA
import busio
import drivers
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60
display = drivers.Lcd()

MIN_ANGLE        =           0
MAX_ANGLE        =           180

RF_KNEE_PIN      =           0
RF_SHOULDER_PIN  =           1
RF_HIP_PIN       =           2
RB_KNEE_PIN      =           12
RB_SHOULDER_PIN  =           9
RB_HIP_PIN       =           10
LF_KNEE_PIN      =           4
LF_SHOULDER_PIN  =           5
LF_HIP_PIN       =           6
LB_KNEE_PIN      =           8
LB_SHOULDER_PIN  =           13
LB_HIP_PIN       =           14

RF_KNEE_INIT     =           80
RF_SHOULDER_INIT =           90
RF_HIP_INIT      =           82
RB_KNEE_INIT     =           90
RB_SHOULDER_INIT =           60
RB_HIP_INIT      =           80
LF_KNEE_INIT     =           110
LF_SHOULDER_INIT =           110
LF_HIP_INIT      =           70
LB_KNEE_INIT     =           85
LB_SHOULDER_INIT =           80
LB_HIP_INIT      =           87

RF_KNEE          =           servo.Servo(pca1.channels[RF_KNEE_PIN])
RF_SHOULDER      =           servo.Servo(pca1.channels[RF_SHOULDER_PIN])
RF_HIP           =           servo.Servo(pca1.channels[RF_HIP_PIN])
RB_KNEE          =           servo.Servo(pca1.channels[RB_KNEE_PIN])
RB_SHOULDER      =           servo.Servo(pca1.channels[RB_SHOULDER_PIN])
RB_HIP           =           servo.Servo(pca1.channels[RB_HIP_PIN])
LF_KNEE          =           servo.Servo(pca1.channels[LF_KNEE_PIN])
LF_SHOULDER      =           servo.Servo(pca1.channels[LF_SHOULDER_PIN])
LF_HIP           =           servo.Servo(pca1.channels[LF_HIP_PIN])
LB_KNEE          =           servo.Servo(pca1.channels[LB_KNEE_PIN])
LB_SHOULDER      =           servo.Servo(pca1.channels[LB_SHOULDER_PIN])
LB_HIP           =           servo.Servo(pca1.channels[LB_HIP_PIN])

CTRL_INIT        =           [12] 
CTRL_ANGLE       =           [12]

def init_spot():
    RF_KNEE.angle     = RF_KNEE_INIT
    RF_SHOULDER.angle = RF_SHOULDER_INIT
    RF_HIP.angle      = RF_HIP_INIT
    RB_KNEE.angle     = RB_KNEE_INIT
    RB_SHOULDER.angle = RB_SHOULDER_INIT
    RB_HIP.angle      = RB_HIP_INIT
    LF_KNEE.angle     = LF_KNEE_INIT
    LF_SHOULDER.angle = LF_SHOULDER_INIT
    LF_HIP.angle      = LF_HIP_INIT
    LB_KNEE.angle     = LB_KNEE_INIT
    LB_SHOULDER.angle = LB_SHOULDER_INIT
    LB_HIP.angle      = LB_HIP_INIT
    time.sleep(0.1)
    display.lcd_clear()   
    display.lcd_display_string("Initialized")

def sit_spot():
    RF_KNEE.angle     = RF_KNEE_INIT + 30
    RF_HIP.angle      = RF_HIP_INIT - 15

    RB_KNEE.angle     = RB_KNEE_INIT +30
    RB_HIP.angle      = RB_HIP_INIT - 15

    LF_KNEE.angle     = LF_KNEE_INIT - 30
    LF_HIP.angle      = LF_HIP_INIT + 15

    LB_KNEE.angle     = LB_KNEE_INIT - 30
    LB_HIP.angle      = LB_HIP_INIT + 15

def returnInit():
    LB_KNEE.angle     = LB_KNEE_INIT
    LB_HIP.angle      = LB_HIP_INIT

    RB_KNEE.angle     = RB_KNEE_INIT
    RB_HIP.angle      = RB_HIP_INIT

    time.sleep(0.1)

    RF_KNEE.angle     = RF_KNEE_INIT
    RF_HIP.angle      = RF_HIP_INIT 

    LF_KNEE.angle     = LF_KNEE_INIT
    LF_HIP.angle      = LF_HIP_INIT

def main():
    init_spot()
    time.sleep(0.5)
    sit_spot()
    time.sleep(0.5)
    returnInit()
