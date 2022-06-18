# set all servos to initial position
import time
from board import SCL, SDA
import busio
import drivers
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import multiprocessing 
import threading
import math


i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60
# display = drivers.Lcd()

#########################################################################
# Right front knee        CHANNEL NUM : 0         initial position: 80
# Right front shoulder    CHANNEL NUM : 1         initial position: 80
# Right front hip         CHANNEL NUM : 2         initial position: 90
# Right back knee         CHANNEL NUM : 4         initial position: 110
# Right back shoulder     CHANNEL NUM : 5         initial position: 100
# Right back hip          CHANNEL NUM : 6         initial position: 90
# Left back knee          CHANNEL NUM : 8         initial position: 90
# Left back shoulder      CHANNEL NUM : 9         initial position: 100
# Left back hip           CHANNEL NUM : 10        initial position: 85
# Left front knee         CHANNEL NUM : 12        initial position: 90
# Left front shoulder     CHANNEL NUM : 13        initial position: 65
# left front hip          CHANNEL NUM : 14        initial position: 83
RF_KNEE_INIT     =           80
RF_SHOULDER_INIT =           90
RF_HIP_INIT      =           90
RB_KNEE_INIT     =           85
RB_SHOULDER_INIT =           70
RB_HIP_INIT      =           90
LF_KNEE_INIT     =           110
LF_SHOULDER_INIT =           100
LF_HIP_INIT      =           85
LB_KNEE_INIT     =           90
LB_SHOULDER_INIT =           80
LB_HIP_INIT      =           88
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

# RF_KNEE_INIT     =           60
# RF_SHOULDER_INIT =           100
# RF_HIP_INIT      =           110
# RB_KNEE_INIT     =           60
# RB_SHOULDER_INIT =           90
# RB_HIP_INIT      =           100
# LF_KNEE_INIT     =           80
# LF_SHOULDER_INIT =           120
# LF_HIP_INIT      =           60
# LB_KNEE_INIT     =           60
# LB_SHOULDER_INIT =           120
# LB_HIP_INIT      =           75


# ---------------------------------------------------------------
# class SpotServo:
#     def __init__(self, servoPin[3]):
#         self.servoPin[3]   = servoPin[3]
#         self.servoKNEE     = servo.Servo(pca1.channels[self.servoPin[0]])
#         self.servoSHLDR    = servo.Servo(pca1.channels[self.servoPin[1]])
#         self.servoHIP      = servo.Servo(pca1.channels[self.servoPin[2]])
        
#     def _set_servo(self, position[3]):
#         for i in range(3):
#             self.servoKNEE.angle  = position[i]
#             self.servoSHLDR.angle = position[i]
#             self.servoHIP.angle   = position[i]
            
# def init_spot():
#     RF_Servo = SpotServo([RF_KNEE_PIN, RF_SHOULDER_PIN, RF_HIP_PIN])
#     RB_Servo = SpotServo([RB_KNEE_PIN, RB_SHOULDER_PIN, RB_HIP_PIN])
#     LF_Servo = SpotServo([LF_KNEE_PIN, LF_SHOULDER_PIN, LF_HIP_PIN])
#     LB_Servo = SpotServo([LB_KNEE_PIN, LB_SHOULDER_PIN, LB_HIP_PIN])
#     time.sleep(0.1)
#     display.lcd_clear()   
#     display.lcd_display_string("Initialized")

# def SPOT_THREAD_INIT():
    
#     RF = threading.Thread(target=RF_Servo._set_servo, args=([RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT]))
#     RB = threading.Thread(target=RB_Servo._set_servo, args=([RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT]))
#     LF = threading.Thread(target=LF_Servo._set_servo, args=([LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT]))
#     LB = threading.Thread(target=LB_Servo._set_servo, args=([LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT]))
#     RF.start()
#     RB.start()
#     LF.start()
#     LB.start()

#     # NOT SURE IF THIS WORKS SIMULANEOUSLY
#     # RF = threading.Thread(target=RF_Servo._set_servo, args=([RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT])).start()
#     # RB = threading.Thread(target=RB_Servo._set_servo, args=([RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT])).start()
#     # LF = threading.Thread(target=LF_Servo._set_servo, args=([LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT])).start()
#     # LB = threading.Thread(target=LB_Servo._set_servo, args=([LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT])).start()
#     # WAIT FOR THREAD TO END
#     # RF.join()
#     # RB.join()
#     # LF.join()
#     # LB.join()

# def ctrl_spot(angle[12]):
#     RF = threading.Thread(target=RF_Servo._set_servo, args=([angle[0], angle[1], angle[2]]))
#     RB = threading.Thread(target=RB_Servo._set_servo, args=([angle[3], angle[4], angle[5]]))
#     LF = threading.Thread(target=LF_Servo._set_servo, args=([angle[6], angle[7], angle[8]]))
#     LB = threading.Thread(target=LB_Servo._set_servo, args=([angle[9], angle[10], angle[12]]))
#     RF.start()
#     RB.start()
#     LF.start()
#     LB.start()

#     # NOT SURE IF THIS WORKS SIMULANEOUSLY
#     # RF = threading.Thread(target=RF_Servo._set_servo, args=([angle[0], angle[1], angle[2]])).start()
#     # RB = threading.Thread(target=RB_Servo._set_servo, args=([angle[3], angle[4], angle[5]])).start()
#     # LF = threading.Thread(target=LF_Servo._set_servo, args=([angle[6], angle[7], angle[8]])).start()
#     # LB = threading.Thread(target=LB_Servo._set_servo, args=([angle[9], angle[10], angle[12]])).start()
#     # WAIT FOR THREAD TO END
#     # RF.join()
#     # RB.join()
#     # LF.join()
#     # LB.join()

# # example
# # ctrl_spot([10,10,10,10,10,10,10,10,10,10,10,10])

# ---------------------------------------------------------------

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
    # display.lcd_clear()   
    # display.lcd_display_string("Initialized",1)

def slow_increment(prev_angle[3],post_angle[3], KNEE, SHOULDER, HIP, step=1):
    offset1 = abs(prev_angle[0] - post_angle[0])
    offset2 = abs(prev_angle[1] - post_angle[1])
    offset3 = abs(prev_angle[2] - post_angle[2])

    print("nothing")


def ctrl_RF(lock, RF_KNEE_ANG, RF_SHOULDER_ANG, RF_HIP_ANG):
    lock.acquire()
    # time.sleep(0.3)
    RF_KNEE.angle = RF_KNEE_ANG
    RF_SHOULDER.angle = RF_SHOULDER_ANG
    RF_HIP.angle = RF_HIP_ANG
    print("ctrl_RF")
    lock.release()
    print("ctrl_RF")

def ctrl_RB(RB_KNEE_ANG, RB_SHOULDER_ANG, RB_HIP_ANG):
    # time.sleep(0.2)
    RB_KNEE.angle = RB_KNEE_ANG
    RB_SHOULDER.angle = RB_SHOULDER_ANG
    RB_HIP.angle = RB_HIP_ANG
    print("ctrl_RB")

def ctrl_LF(LF_KNEE_ANG, LF_SHOULDER_ANG, LF_HIP_ANG):
    # time.sleep(0.1)
    LF_KNEE.angle = LF_KNEE_ANG
    LF_SHOULDER.angle = LF_SHOULDER_ANG
    LF_HIP.angle = LF_HIP_ANG
    print("ctrl_LF")

def ctrl_LB(LB_KNEE_ANG, LB_SHOULDER_ANG, LB_HIP_ANG):
    LB_KNEE.angle = LB_KNEE_ANG
    LB_SHOULDER.angle = LB_SHOULDER_ANG
    LB_HIP.angle = LB_HIP_ANG
    print("ctrl_LB")

def SPOT_THREAD_INIT():
    lock = multiprocessing.Lock()
    e = multiprocessing.Event()
    print("event") 
    RF = multiprocessing.Process(target=ctrl_RF, args=(lock,RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT))
    RB = multiprocessing.Process(target=ctrl_RB, args=(RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT))
    LF = multiprocessing.Process(target=ctrl_LF, args=(LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT))
    LB = multiprocessing.Process(target=ctrl_LB, args=(LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT))
    print("event") 

    
    RB.start()
    print("rb")
    RF.start()
    print("rf")
    LF.start()
    print("lf")
    LB.start()
    print("lb")

    e.set()

    # RF.join()
    # RB.join()
    # LF.join()
    # LB.join()

    print("SPOT_THREAD_INIT")
    return(RF, RB,LF,LB)




def main():

    [RF, RB,LF,LB]=SPOT_THREAD_INIT()
    # display.lcd_display_string("   INIT POSE   ", 1) 
    init_spot()
    pca1.deinit()


if __name__ == '__main__':
    main()







'''
fingers = [] # empty list of fingers
for i in range(5):
	t = Hardware() # create a finger
	fingers.append(t) # add it to the list
# you now have 5 fingers
'''

'''
def do_something():
    print('Sleeping 1 seconds')
    time.sleep(1)
    print('Done Sleeping...')
 
if __name__ == '__main__':

    threads = []
    for _ in range(10): # 10 reps
        t = threading.Thread(target=do_something)
        t.start()
        threads.append(t)
        
    for thread in threads:
        thread.join()
'''
