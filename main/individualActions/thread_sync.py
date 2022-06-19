# set all servos to initial position
import time
from board import SCL, SDA
import busio
import drivers
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import threading

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60
display = drivers.Lcd()

#################### you do not cange these ############################
MIN_ANGLE        =           0
MAX_ANGLE        =           180

RF_KNEE_PIN      =           0
RF_SHOULDER_PIN  =           1
RF_HIP_PIN       =           2
RB_KNEE_PIN      =           4
RB_SHOULDER_PIN  =           5
RB_HIP_PIN       =           6
LF_KNEE_PIN      =           8
LF_SHOULDER_PIN  =           9
LF_HIP_PIN       =           10
LB_KNEE_PIN      =           12
LB_SHOULDER_PIN  =           13
LB_HIP_PIN       =           14

RF_LEG           =   [RF_KNEE_PIN, RF_SHOULDER_PIN, RF_HIP_PIN]
RB_LEG           =   [RB_KNEE_PIN, RB_SHOULDER_PIN, RB_HIP_PIN]
LF_LEG           =   [LF_KNEE_PIN, LF_SHOULDER_PIN, LF_HIP_PIN]
LB_LEG           =   [LB_KNEE_PIN, LB_SHOULDER_PIN, LB_HIP_PIN]

RF_KNEE_INIT     =           80
RF_SHOULDER_INIT =           80
RF_HIP_INIT      =           90
RB_KNEE_INIT     =           110
RB_SHOULDER_INIT =           100
RB_HIP_INIT      =           90
LF_KNEE_INIT     =           90
LF_SHOULDER_INIT =           100
LF_HIP_INIT      =           85
LB_KNEE_INIT     =           90
LB_SHOULDER_INIT =           65
LB_HIP_INIT      =           83
######################################################################

class SpotServo:
    def __init__(self, servoPin[3]):
        self.servoPin[3]   = servoPin[3]
        self.servoPos[3]   = [0, 0, 0]
        self.servoKNEE     = servo.Servo(pca1.channels[self.servoPin[0]])
        self.servoSHLDR    = servo.Servo(pca1.channels[self.servoPin[1]])
        self.servoHIP      = servo.Servo(pca1.channels[self.servoPin[2]])
        
    def _set_servo(self, position[3]):
        self.servoKNEE.angle  = position[0]
        self.servoSHLDR.angle = position[1]
        self.servoHIP.angle   = position[2]

    def target_position(self, target[3], delay=0):
        """set all servo to a position which needs to be reached after delay second"""
        if delay < 0.02:
            # set all servo immediately to position
            for k in range(3):
                # set servo position for servo 'k'
                self._set_servo(target[3])
        else:
            ddelay = 0.02 # 20 ms are servo period time
            iterations = int( delay / ddelay)  
            # if number of iterations is too high, then decrease time resolution a bit
            if iterations > 32:
                ddelay = 0.04
                iterations = int( delay / ddelay) 
            for i in range(iterations):
                pos[3] = [0, 0, 0]
                for k in range(3):
                    # set servo position for servo 'k'
                    pos[k] = (target[k] - self.servo_pos[k]) / iterations * i
                self._set_servo(pos[3])
                time.sleep(ddelay)
        
        self.servo_pos = target[3]
    
    # 3 servo 
    def slow_offset(self, prev_angle[3], post_angle[3], servo, step = 1):
        for i in range(3):
            offset[i] = abs(prev_angle[i] - post_angle[i])
    
        if(prev_angle < post_angle):
            for i in range(1, offset, step):
                servo.angle(prev_angle+i)
        elif(prev_angle > post_angle):
            for i in range(1, offset, step):
                servo.angle(prev_angle-i)
        else:
            display.lcd_display_string("I do not move!", 1)
            
def init_spot():
    RF_Servo = SpotServo(RF_LEG)
    RB_Servo = SpotServo(RB_LEG)
    LF_Servo = SpotServo(LF_LEG)
    LB_Servo = SpotServo(LB_LEG)
    time.sleep(0.1)
    display.lcd_clear()   
    display.lcd_display_string("Initialized")
    return RF_Servo, RB_Servo, LF_Servo, LB_Servo

def init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo):
    RF = threading.Thread(target=RF_Servo._set_servo, args=([RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT]))
    RB = threading.Thread(target=RB_Servo._set_servo, args=([RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT]))
    LF = threading.Thread(target=LF_Servo._set_servo, args=([LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT]))
    LB = threading.Thread(target=LB_Servo._set_servo, args=([LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT]))
    RF.start()
    RB.start()
    LF.start()
    LB.start()

def ctrl_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo, angle[12]):
    RF = threading.Thread(target=RF_Servo.target_position, args=([angle[0], angle[1], angle[2]]))
    RB = threading.Thread(target=RB_Servo.target_position, args=([angle[3], angle[4], angle[5]]))
    LF = threading.Thread(target=LF_Servo.target_position, args=([angle[6], angle[7], angle[8]]))
    LB = threading.Thread(target=LB_Servo.target_position, args=([angle[9], angle[10], angle[12]]))
    RF.start()
    RB.start()
    LF.start()
    LB.start()

# [RF_Servo, RB_Servo, LF_Servo, LB_Servo] = init_spot()
# init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo)
# target[12] = [90,90,90,90,90,90,90,90,90,90,90,90]
# ctrl_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo, target[12])



def main():
    [RF_Servo, RB_Servo, LF_Servo, LB_Servo] = init_spot()
    init_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo)
    target[12] = [90,90,90,90,90,90,90,90,90,90,90,90]
    ctrl_pos_spot(RF_Servo, RB_Servo, LF_Servo, LB_Servo, target[12])
    display.lcd_display_string("   INIT POSE   ", 1) 
    pca1.deinit()


if __name__ == '__main__':
    main()



