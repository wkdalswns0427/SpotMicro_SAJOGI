# set all servos to initial position
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
#########################################################################
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


def main():
    display.lcd_display_string("   INIT POSE   ", 1) 
    init_spot()
    pca1.deinit()


if __name__ == '__main__':
    main()

'''
import time

class Hardware:
    def __init__(self):
        self.N = 5
        self.servo_pos = [0,0,0,0,0]
        self.kit = .... initialization of driver
        
    def _set_servo(self, servo, position):
        """ set single servo [0...N-1] to a position"""
        # print("servo", servo, "to", position)
        self.kit.servo[servo].angle = position
        
    def target_position(self, p0, p1, p2, p3, p4, delay=0):
        """set all servo to a position which needs to be reached after delay second"""
            
        new_pos =  [p0, p1, p2, p3, p4]
        if delay < 0.02:
            # set all servo immediately to position
            for k in range(self.N):
                # set servo position for servo 'k'
                self._set_servo(k, new_pos[k] )
        else:
            ddelay = 0.02 # 20 ms are servo period time
            iterations = int( delay / ddelay)  
            # if number of iterations is too high, then decrease time resolution a bit
            if iterations > 32:
                ddelay = 0.04
                iterations = int( delay / ddelay) 
                
            for i in range(iterations):
                for k in range(self.N):
                    # set servo position for servo 'k'
                    pos = (new_pos[k] - self.servo_pos[k]) / iterations * i
                    self._set_servo(k, pos)
                
                time.sleep(ddelay)
        
        self.servo_pos = new_pos
        
# example usage

hardware = Hardware()
hardware.target_position(10, -20, 22, -60, 100, delay=10.0)








from adafruit_servokit import ServoKit
import threading
import time
kit = ServoKit(channels=16)

def thumbFinger(fingerAngle, fingerDelay):
    for fingerAngle in range (0,180):
        kit.servo[1].angle = fingerAngle
        time.sleep(fingerDelay)
        print(fingerAngle, fingerDelay)

def indexFinger(fingerAngle, fingerDelay):
    for fingerAngle in range (0,180):
        kit.servo[2].angle = fingerAngle
        time.sleep(fingerDelay)
        print(fingerAngle, fingerDelay)


if __name__ == "__main__":
    t1 = threading.Thread(target=thumbFinger, args=(180,0.01))
    t2 = threading.Thread(target=indexFinger, args=(180,0.01))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
'''