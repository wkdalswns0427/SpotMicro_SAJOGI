import time
from threading import Thread
import sys
from board import SCL, SDA
import busio
import config as cf
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60

RF_LEG_PIN = cf.RF_LEG
RB_LEG_PIN = cf.RB_LEG
LF_LEG_PIN = cf.LF_LEG
LB_LEG_PIN = cf.LB_LEG

RF_LEG_INIT = cf.RF_LEG_INIT
RB_LEG_INIT = cf.RB_LEG_INIT
LF_LEG_INIT = cf.LF_LEG_INIT
LB_LEG_INIT = cf.LB_LEG_INIT

RF_LEG_FWD = cf.RF_LEG_FWD
RB_LEG_FWD = cf.RB_LEG_FWD
LF_LEG_FWD = cf.LF_LEG_FWD
LB_LEG_FWD = cf.LB_LEG_FWD

class A_LEG:
    def __init__(self, motor, number = 0):
        self.servoHIP = servo.Servo(pca1.channels[motor[2]])
        self.servoSHLDR = servo.Servo(pca1.channels[motor[1]])
        self.servoKNEE = servo.Servo(pca1.channels[motor[0]])
        self.targetAngle = [0,0,0]
        self.legNum = number
    
    def _set_servo(self, position, time_lag=[0,0,0], leg_lag=0):
        self.servoKNEE.angle  = position[0]
        time.sleep(time_lag[0] + leg_lag)
        self.servoSHLDR.angle = position[1]
        time.sleep(time_lag[1] + leg_lag)
        self.servoHIP.angle   = position[2]
        time.sleep(time_lag[2] + leg_lag)
    
    def _pos_init(self, position):
        self.servoKNEE.angle  = position[0]
        self.servoSHLDR.angle = position[1]
        self.servoHIP.angle   = position[2]

    def _fwd_step(self, position, return_position, time_lag=[0,0,0], leg_lag=0):
        self.servoKNEE.angle  = position[0]
        time.sleep(time_lag[0] + leg_lag)
        self.servoSHLDR.angle = position[1]
        time.sleep(time_lag[1] + leg_lag)
        self.servoHIP.angle   = position[2]
        time.sleep(time_lag[2] + leg_lag)

        self.servoKNEE.angle  = return_position[0]
        self.servoSHLDR.angle = return_position[1]
        self.servoHIP.angle   = return_position[2]

def configLegs():
    RF_LEG_SET = A_LEG(RF_LEG_PIN, 0)
    RB_LEG_SET = A_LEG(RB_LEG_PIN, 1)
    LF_LEG_SET = A_LEG(LF_LEG_PIN, 2)
    LB_LEG_SET = A_LEG(LB_LEG_PIN, 3)
    return RF_LEG_SET,RB_LEG_SET,LF_LEG_SET,LB_LEG_SET

def init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo):
    RF_Servo._pos_init(RF_LEG_INIT)
    RB_Servo._pos_init(RB_LEG_INIT)
    LF_Servo._pos_init(LF_LEG_INIT)
    LB_Servo._pos_init(LB_LEG_INIT)

def walk_fwd(RF_Servo, RB_Servo, LF_Servo, LB_Servo):
    RF = Thread(target=RF_Servo._set_servo, args = (RF_LEG_FWD,0,0))
    LB = Thread(target=LB_Servo._set_servo, args = (LB_LEG_FWD,0,0))
    LF = Thread(target=LF_Servo._set_servo, args = ())
    RB = Thread(target=RB_Servo._set_servo, args = ())
    RF.start()
    LB.start()
    LF.start()
    RB.start()


def main():
    RF_Servo, RB_Servo, LF_Servo, LB_Servo= configLegs()
    print("leg classes configured")
    init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo)
    print("initial pose")
    time.sleep(1)
    '''
    Move code here
    '''
    init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo)
    print("Spot deinitialized")

if __name__ == '__main__':
    main()