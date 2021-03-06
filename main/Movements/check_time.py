import time
# from requests import post
from board import SCL, SDA
import busio
import drivers
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
# import threading
import timeit

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60
# display = drivers.Lcd()

#########################################################################
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

RF_KNEE_INIT     =           82
RF_SHOULDER_INIT =           90
RF_HIP_INIT      =           75
RB_KNEE_INIT     =           100
RB_SHOULDER_INIT =           60
RB_HIP_INIT      =           83
LF_KNEE_INIT     =           107
LF_SHOULDER_INIT =           107
LF_HIP_INIT      =           69
LB_KNEE_INIT     =           75
LB_SHOULDER_INIT =           80
LB_HIP_INIT      =           85

RF_LEG           =   [RF_KNEE_PIN, RF_SHOULDER_PIN, RF_HIP_PIN]
RB_LEG           =   [RB_KNEE_PIN, RB_SHOULDER_PIN, RB_HIP_PIN]
LF_LEG           =   [LF_KNEE_PIN, LF_SHOULDER_PIN, LF_HIP_PIN]
LB_LEG           =   [LB_KNEE_PIN, LB_SHOULDER_PIN, LB_HIP_PIN]

RF_LEG_INIT = [RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT]
RB_LEG_INIT = [RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT]
LF_LEG_INIT = [LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT]
LB_LEG_INIT = [LB_KNEE_INIT, LB_SHOULDER_INIT , LB_HIP_INIT]

RF_LAG_TIME = [0.015, 0, 0.01]
RB_LAG_TIME = [0, 0.015, 0.01]
LF_LAG_TIME = [0, 0.015, 0.022]
LB_LAG_TIME = [0, 0.005, 0.015]
#########################################################################

# RF_KNEE          =           servo.Servo(pca1.channels[RF_KNEE_PIN])
# RF_SHOULDER      =           servo.Servo(pca1.channels[RF_SHOULDER_PIN])
# RF_HIP           =           servo.Servo(pca1.channels[RF_HIP_PIN])
# RB_KNEE          =           servo.Servo(pca1.channels[RB_KNEE_PIN])
# RB_SHOULDER      =           servo.Servo(pca1.channels[RB_SHOULDER_PIN])
# RB_HIP           =           servo.Servo(pca1.channels[RB_HIP_PIN])
# LF_KNEE          =           servo.Servo(pca1.channels[LF_KNEE_PIN])
# LF_SHOULDER      =           servo.Servo(pca1.channels[LF_SHOULDER_PIN])
# LF_HIP           =           servo.Servo(pca1.channels[LF_HIP_PIN])
# LB_KNEE          =           servo.Servo(pca1.channels[LB_KNEE_PIN])
# LB_SHOULDER      =           servo.Servo(pca1.channels[LB_SHOULDER_PIN])
# LB_HIP           =           servo.Servo(pca1.channels[LB_HIP_PIN])

INIT_POSITION = [
    RF_KNEE_INIT,RF_SHOULDER_INIT,RF_HIP_INIT,
    RB_KNEE_INIT,RB_SHOULDER_INIT,RB_HIP_INIT,
    LF_KNEE_INIT,LF_SHOULDER_INIT,LF_HIP_INIT,
    LB_KNEE_INIT,LB_SHOULDER_INIT,LB_HIP_INIT 
]

PREV_BUFFER = [
    RF_KNEE_INIT,RF_SHOULDER_INIT,RF_HIP_INIT,
    RB_KNEE_INIT,RB_SHOULDER_INIT,RB_HIP_INIT,
    LF_KNEE_INIT,LF_SHOULDER_INIT,LF_HIP_INIT,
    LB_KNEE_INIT,LB_SHOULDER_INIT,LB_HIP_INIT 
]

class A_LEG:
    def __init__(self, motor, number = 0):
        self.servoHIP = servo.Servo(pca1.channels[motor[2]])
        self.servoSHLDR = servo.Servo(pca1.channels[motor[1]])
        self.servoKNEE = servo.Servo(pca1.channels[motor[0]])
        self.targetAngle = [0,0,0]
        self.legNum = number
    
    def _set_servo(self, position, time_lag, leg_lag):
        self.servoKNEE.angle  = position[0]
        time.sleep(time_lag[0] + leg_lag)

        self.servoSHLDR.angle = position[1]
        time.sleep(time_lag[1] + leg_lag)

        self.servoHIP.angle   = position[2]
        time.sleep(time_lag[2] + leg_lag)

        # print(self.servoKNEE.angle)
        # print(self.servoSHLDR.angle)
        # print(self.servoHIP.angle)

    def target_position(self, prev_angle, post_angle, step = 1):
        offset = [0,0,0]
        diff = [0,0,0]
        addup = [0,0,0]
        cnt = [0,0,0]
        abscnt = 1
        fincnt = 0
        
        for i in range(0,2):
            diff[i] = prev_angle[i] - post_angle[i]
            offset[i] = abs(prev_angle[i] - post_angle[i])
        
        for i in range(0,2):
            if diff[i]>0:
                addup[i] = -1
            elif diff[i]<0:
                addup[i] = 1
        
        while cnt[0]<=offset[0] or cnt[1]<=offset[1] or cnt[2]<=offset[2]:
            for i in range(0,2):
                if cnt[i]<=offset[i]:
                    addup[i] = addup[i]*abscnt
                else:
                    addup[i] = 0

            self.servoKNEE.angle  = prev_angle[0] + addup[0]*step
            self.servoSHLDR.angle = prev_angle[1] + addup[1]*step
            self.servoHIP.angle   = prev_angle[2] + addup[2]*step
            abscnt += 1
            
            for i in range(0,2):
                cnt[i]+=1
            
        for i in range(self.legNum, self.legNum+2):
            PREV_BUFFER[i] = prev_angle[0+fincnt] + addup[0+fincnt]
            fincnt += 1

    def move_a_leg(self, hipAngle, shoulderAngle, kneeAngle):
        self.targetAngle = [hipAngle,shoulderAngle,kneeAngle]
        self.target_position(self, PREV_BUFFER, self.targetAngle, 1)

def configLegs():
    RF_LEG_SET = A_LEG(RF_LEG, 0)
    RB_LEG_SET = A_LEG(RB_LEG, 1)
    LF_LEG_SET = A_LEG(LF_LEG, 2)
    LB_LEG_SET = A_LEG(LB_LEG, 3)

    return RF_LEG_SET,RB_LEG_SET,LF_LEG_SET,LB_LEG_SET

def init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo):
    RF_Servo._set_servo(RF_LEG_INIT, RF_LAG_TIME, 0.018)
    RB_Servo._set_servo(RB_LEG_INIT, RB_LAG_TIME, 0)
    LF_Servo._set_servo(LF_LEG_INIT, LF_LAG_TIME, 0.018)
    LB_Servo._set_servo(LB_LEG_INIT, LB_LAG_TIME, 0.01)

def ctrl_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo, prev_angle = INIT_POSITION, post_angle = INIT_POSITION):
    RF_Servo.target_position([prev_angle[0], prev_angle[1], prev_angle[2]], [post_angle[0], post_angle[1], post_angle[2]],1)
    RB_Servo.target_position([prev_angle[3], prev_angle[4], prev_angle[5]], [post_angle[3], post_angle[4], post_angle[5]],1)
    LF_Servo.target_position([prev_angle[6], prev_angle[7], prev_angle[8]], [post_angle[6], post_angle[7], post_angle[8]],1)
    LB_Servo.target_position([prev_angle[9], prev_angle[10], prev_angle[11]], [post_angle[9], post_angle[10], post_angle[11]],1)

'''
def intial_position():
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
    #display.lcd_clear()   
    #display.lcd_display_string("Initialized",1)

def one_step_forward():
    # two legs in diagonal forward
    RF_KNEE.angle = RF_KNEE_INIT - 10
    LB_KNEE.angle = LB_KNEE_INIT + 10
    time.sleep(0.03)
    # time.sleep(0.03)

    RF_SHOULDER.angle = RF_SHOULDER_INIT - 25
    LB_SHOULDER.angle = LB_SHOULDER_INIT + 25

    RB_SHOULDER.angle = RB_SHOULDER_INIT + 25 #
    LF_SHOULDER.angle = LF_SHOULDER_INIT + 25 #

    RB_KNEE.angle = RB_KNEE_INIT + 15
    LF_KNEE.angle = LF_KNEE_INIT - 15
    # time.sleep(0.03)
    time.sleep(0.03)


    RF_KNEE.angle = RF_KNEE_INIT + 15
    LB_KNEE.angle = LB_KNEE_INIT - 15
    # time.sleep(0.03)
    time.sleep(0.03)

    RF_SHOULDER.angle = RF_SHOULDER_INIT
    LB_SHOULDER.angle = LB_SHOULDER_INIT
    RB_SHOULDER.angle = RB_SHOULDER_INIT 
    LF_SHOULDER.angle = LF_SHOULDER_INIT 
    RF_KNEE.angle = RF_KNEE_INIT
    LB_KNEE.angle = LB_KNEE_INIT
    # time.sleep(0.03)
    time.sleep(0.03)

    RB_KNEE.angle = RB_KNEE_INIT - 10
    LF_KNEE.angle = LF_KNEE_INIT + 10
    # time.sleep(0.03)
    time.sleep(0.03)

    RB_SHOULDER.angle = RB_SHOULDER_INIT - 25
    LF_SHOULDER.angle = LF_SHOULDER_INIT + 25

    RF_SHOULDER.angle = RF_SHOULDER_INIT - 25 #
    LB_SHOULDER.angle = LB_SHOULDER_INIT - 25 #

    RF_KNEE.angle = RF_KNEE_INIT + 15
    LB_KNEE.angle = LB_KNEE_INIT - 15
    # time.sleep(0.03)
    time.sleep(0.03)

    RB_KNEE.angle = RB_KNEE_INIT + 15
    LF_KNEE.angle = LF_KNEE_INIT - 15
    # time.sleep(0.03)
    time.sleep(0.03)

    RF_SHOULDER.angle = RF_SHOULDER_INIT
    LB_SHOULDER.angle = LB_SHOULDER_INIT
    RB_KNEE.angle = RB_KNEE_INIT
    LF_KNEE.angle = LF_KNEE_INIT
    RB_SHOULDER.angle = RB_SHOULDER_INIT
    LF_SHOULDER.angle = LF_SHOULDER_INIT
    # time.sleep(0.03)
    time.sleep(0.03)
'''

def main():

    start = time.time()

    RF_Servo, RB_Servo, LF_Servo, LB_Servo= configLegs()
    print("leg classes configured")

    init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo)
    print("initial pose")

    # print("Setting up with 3")
    # time.sleep(1)
    # print("2")
    # time.sleep(1)
    # print("1")

    # print("Start time = " + str(time.time()))
    # RB_Servo._set_servo([RB_KNEE_INIT + 20, RB_SHOULDER_INIT + 20, RB_HIP_INIT + 20], RB_LAG_TIME, 0)
    # LB_Servo._set_servo([LB_KNEE_INIT + 20, LB_SHOULDER_INIT + 20, LB_HIP_INIT + 20], LB_LAG_TIME, 0)
    # RF_Servo._set_servo([RF_KNEE_INIT + 20, RF_SHOULDER_INIT + 20, RF_HIP_INIT + 20], RF_LAG_TIME, 0)
    # LF_Servo._set_servo([LF_KNEE_INIT + 20, LF_SHOULDER_INIT + 20, LF_HIP_INIT + 20], LF_LAG_TIME, 0)
    # # time.sleep(0)
    
    # # time.sleep(0.018)
    # # time.sleep(0.01)
    # print("End time = " + str(time.time()))

    # time.sleep(3)
    # init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo)

    print("done")

if __name__ == '__main__':
    main()