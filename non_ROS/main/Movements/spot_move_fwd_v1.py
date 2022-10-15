# set all servos to initial position
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import config as cf

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60
# display = drivers.Lcd()

RF_LEG_PIN = cf.RF_LEG_PIN
RB_LEG_PIN = cf.RB_LEG_PIN
LF_LEG_PIN = cf.LF_LEG_PIN
LB_LEG_PIN = cf.LB_LEG_PIN

RF_LEG_INIT = cf.RF_LEG_INIT
RB_LEG_INIT = cf.RB_LEG_INIT
LF_LEG_INIT = cf.LF_LEG_INIT
LB_LEG_INIT = cf.LB_LEG_INIT


RF_KNEE          =           servo.Servo(pca1.channels[cf.RF_KNEE_PIN])
RF_SHOULDER      =           servo.Servo(pca1.channels[cf.RF_SHOULDER_PIN])
RF_HIP           =           servo.Servo(pca1.channels[cf.RF_HIP_PIN])
RB_KNEE          =           servo.Servo(pca1.channels[cf.RB_KNEE_PIN])
RB_SHOULDER      =           servo.Servo(pca1.channels[cf.RB_SHOULDER_PIN])
RB_HIP           =           servo.Servo(pca1.channels[cf.RB_HIP_PIN])
LF_KNEE          =           servo.Servo(pca1.channels[cf.LF_KNEE_PIN])
LF_SHOULDER      =           servo.Servo(pca1.channels[cf.LF_SHOULDER_PIN])
LF_HIP           =           servo.Servo(pca1.channels[cf.LF_HIP_PIN])
LB_KNEE          =           servo.Servo(pca1.channels[cf.LB_KNEE_PIN])
LB_SHOULDER      =           servo.Servo(pca1.channels[cf.LB_SHOULDER_PIN])
LB_HIP           =           servo.Servo(pca1.channels[cf.LB_HIP_PIN])


def init_spot():
    RF_KNEE.angle     = cf.RF_KNEE_INIT
    RF_SHOULDER.angle = cf.RF_SHOULDER_INIT
    RF_HIP.angle      = cf.RF_HIP_INIT
    RB_KNEE.angle     = cf.RB_KNEE_INIT
    RB_SHOULDER.angle = cf.RB_SHOULDER_INIT
    RB_HIP.angle      = cf.RB_HIP_INIT
    LF_KNEE.angle     = cf.LF_KNEE_INIT
    LF_SHOULDER.angle = cf.LF_SHOULDER_INIT
    LF_HIP.angle      = cf.LF_HIP_INIT
    LB_KNEE.angle     = cf.LB_KNEE_INIT
    LB_SHOULDER.angle = cf.LB_SHOULDER_INIT
    LB_HIP.angle      = cf.LB_HIP_INIT
    time.sleep(0.1)
    
def stepfwd():
    # RF fwd
    LF_KNEE.angle = LF_LEG_INIT[0]+15
    RB_KNEE.angle = RB_LEG_INIT[0]-15
    LB_KNEE.angle = LB_LEG_INIT[0]-15
    time.sleep(0.1)
    RF_SHOULDER.angle = RF_LEG_INIT[1] - 20 
    RF_KNEE.angle = RF_LEG_INIT[0] + 15
    LB_KNEE.angle = LB_LEG_INIT[0]
    time.sleep(0.1)
    RF_SHOULDER.angle = RF_LEG_INIT[1]
    RF_KNEE.angle = RF_LEG_INIT[0]
    time.sleep(0.1)
    LB_SHOULDER.angle = LB_LEG_INIT[1] + 20
    LB_KNEE.angle = LB_LEG_INIT[0] - 15
    LF_KNEE.angle = LF_LEG_INIT[0]
    time.sleep(0.1)
    RB_KNEE.angle = RB_LEG_INIT[0]
    LB_SHOULDER.angle = LB_LEG_INIT[1]
    LF_KNEE.angle = LF_LEG_INIT[0] + 15
    time.sleep(0.1)
    RF_KNEE.angle = RF_LEG_INIT[0] + 15
    LF_SHOULDER.angle = LF_LEG_INIT[1] + 20
    LF_KNEE.angle = LF_LEG_INIT[0] - 15 
    LF_SHOULDER.angle = LF_LEG_INIT[1]
    LF_KNEE.angle = LF_LEG_INIT[0]
    time.sleep(0.1)
    RB_KNEE.angle = RB_LEG_INIT[0]
    RB_SHOULDER.angle = RB_LEG_INIT[1] + 20
    RB_KNEE.angle = RB_LEG_INIT[0] - 15
    time.sleep(0.1)
    RB_SHOULDER.angle = RB_LEG_INIT[1]
    RB_KNEE.angle = RB_LEG_INIT[0]
    time.sleep(0.1)
    RF_KNEE.angle = RF_LEG_INIT[0]
    LB_KNEE.angle = LB_LEG_INIT[0]


def slidefwd():
    RF_SHOULDER.angle = RF_LEG_INIT[1] - 10
    LF_SHOULDER.angle = LF_LEG_INIT[1] + 10
    time.sleep(0.1)
    RB_KNEE.angle = RB_LEG_INIT[0] - 10
    LB_KNEE.angle = LB_LEG_INIT[0] + 10
    time.sleep(0.1)
    RF_KNEE.angle = RB_LEG_INIT[0] + 10
    LF_KNEE.angle = LB_LEG_INIT[0] - 10
    time.sleep(0.1)
    RF_SHOULDER.angle = RF_LEG_INIT[1] + 10
    LF_SHOULDER.angle = LF_LEG_INIT[1] - 10
    time.sleep(0.1)
    RB_SHOULDER.angle = RB_LEG_INIT[1] + 10
    LB_SHOULDER.angle = LB_LEG_INIT[1] - 10
    time.sleep(0.1)
    RB_KNEE.angle = RB_LEG_INIT[0]
    LB_KNEE.angle = LB_LEG_INIT[0]
    time.sleep(0.1)
    RF_KNEE.angle = RF_LEG_INIT[0] - 10
    LF_KNEE.angle = LF_LEG_INIT[0] + 10
    time.sleep(0.1)
    RF_SHOULDER.angle = RF_LEG_INIT[1]
    LF_SHOULDER.angle = LF_LEG_INIT[1]
    RB_SHOULDER.angle = RB_LEG_INIT[1]
    LB_SHOULDER.angle = LB_LEG_INIT[1]
    RF_KNEE.angle = RF_LEG_INIT[0]
    LF_KNEE.angle = LF_LEG_INIT[0]
    time.sleep(0.1)
  

def main():
    init_spot()
    time.sleep(2)
    for i in range(10):
        slidefwd()
    
    init_spot()
    pca1.deinit()


if __name__ == '__main__':
    print("hi")
    main()
    print("done")

