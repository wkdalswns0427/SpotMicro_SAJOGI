import time
import math
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# I2C 초기화
i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60

# 핀 번호 설정
LF_KNEE_PIN, LF_SHOULDER_PIN, LF_HIP_PIN = 10, 9, 8
LB_KNEE_PIN, LB_SHOULDER_PIN, LB_HIP_PIN = 2, 1, 0
RF_KNEE_PIN, RF_SHOULDER_PIN, RF_HIP_PIN = 14, 13, 12
RB_KNEE_PIN, RB_SHOULDER_PIN, RB_HIP_PIN = 6, 5, 4

# 초기 각도 설정



shoulder2 = 52  #71
knee2	 = 40   #10
shoulder_calib = 5
knee_calib = 6


RF_KNEE_INIT     =           65   + knee2  +knee_calib  # small down  
RF_SHOULDER_INIT =           51   +shoulder2    #small down 
RF_HIP_INIT      =           83 

RB_KNEE_INIT     =           76   +knee2 +knee_calib
RB_SHOULDER_INIT =           56.2   +shoulder2    # small down
RB_HIP_INIT      =           87

LF_KNEE_INIT     =           98    -knee2  -knee_calib  # small up 
LF_SHOULDER_INIT =           118   -shoulder2       # small downS
LF_HIP_INIT      =           94


LB_KNEE_INIT     =           117     -knee2   -knee_calib  # small up 
LB_SHOULDER_INIT =           92.5   -shoulder2
LB_HIP_INIT      =           84



'''
RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT = 90, 135, 80
RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT = 93, 150, 90
LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT = 70, 30, 87
LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT = 90, 45, 90
'''
# 서보 객체 생성

RF_KNEE = servo.Servo(pca1.channels[RF_KNEE_PIN])
RF_SHOULDER = servo.Servo(pca1.channels[RF_SHOULDER_PIN])
RF_HIP = servo.Servo(pca1.channels[RF_HIP_PIN])

RB_KNEE = servo.Servo(pca1.channels[RB_KNEE_PIN])
RB_SHOULDER = servo.Servo(pca1.channels[RB_SHOULDER_PIN])
RB_HIP = servo.Servo(pca1.channels[RB_HIP_PIN])

LB_KNEE = servo.Servo(pca1.channels[LB_KNEE_PIN])
LB_SHOULDER = servo.Servo(pca1.channels[LB_SHOULDER_PIN])
LB_HIP = servo.Servo(pca1.channels[LB_HIP_PIN])


LF_KNEE = servo.Servo(pca1.channels[LF_KNEE_PIN])
LF_SHOULDER = servo.Servo(pca1.channels[LF_SHOULDER_PIN])
LF_HIP = servo.Servo(pca1.channels[LF_HIP_PIN])

def init_spot():
    RF_KNEE.angle, RF_SHOULDER.angle = RF_KNEE_INIT, RF_SHOULDER_INIT
    RB_KNEE.angle, RB_SHOULDER.angle = RB_KNEE_INIT, RB_SHOULDER_INIT
    LF_KNEE.angle, LF_SHOULDER.angle = LF_KNEE_INIT, LF_SHOULDER_INIT
    LB_KNEE.angle, LB_SHOULDER.angle = LB_KNEE_INIT, LB_SHOULDER_INIT
    time.sleep(0.5)

def fwd_step_test(steps=120, delay=0.001):
	LB_KNEE.angle = LB_KNEE_INIT +40
	time.sleep(1)
	LB_SHOULDER.angle = LB_SHOULDER_INIT + 30
	time.sleep(1)
	LB_KNEE.angle = LB_KNEE_INIT - 9
	time.sleep(1)
	
def floor_test(steps = 20, delay=0.005):
	max_deg = 5  # alpha
	min_deg = -4.5 # beta
	alpha = 20
	back_calib = 0
	
	# calc foward point
	x = 51.3 + max_deg
	y = math.degrees(math.acos(1.58 - math.sin(math.radians(x))/1.26)) + 38.7 - max_deg
	fwd_deg = 55.2-y
		
		
	for step in range(steps):
		theta = min_deg * step / steps 
		LB_SHOULDER.angle = LB_SHOULDER_INIT + theta
		RB_SHOULDER.angle = RB_SHOULDER_INIT - theta
		LF_SHOULDER.angle = LF_SHOULDER_INIT + theta
		RF_SHOULDER.angle = RF_SHOULDER_INIT - theta
		x = 51.3 + theta
		y = math.degrees(math.acos(1.58 - math.sin(math.radians(x))/1.26)) + 38.7 - theta
		#print(y)
		delta = 55.2-y
		LB_KNEE.angle = LB_KNEE_INIT -delta - back_calib*step/steps
		RB_KNEE.angle = RB_KNEE_INIT +delta + back_calib*step/steps
		LF_KNEE.angle = LF_KNEE_INIT -delta - back_calib*step/steps
		RF_KNEE.angle = RF_KNEE_INIT +delta + back_calib*step/steps
		time.sleep(delay)
		
	time.sleep(1)
	LB_SHOULDER.angle = LB_SHOULDER_INIT - 5
	RF_SHOULDER.angle = RF_SHOULDER_INIT + 5
	LB_KNEE.angle = LB_KNEE_INIT + 10
	RF_KNEE.angle = RF_KNEE_INIT - 10
	LB_SHOULDER.angle = LB_SHOULDER_INIT + max_deg
	RF_SHOULDER.angle = RF_SHOULDER_INIT - max_deg	
	time.sleep(0.2)
	LB_KNEE.angle = LB_KNEE_INIT - fwd_deg
	RF_KNEE.angle = RF_KNEE_INIT + fwd_deg
	
	
	time.sleep(1)
	# LB RF fwd max_deg
	
	RB_KNEE.angle = RB_KNEE_INIT - alpha
	LF_KNEE.angle = LF_KNEE_INIT + alpha
	
	for step in range(steps*3):
		theta = max_deg - (max_deg-min_deg) * step / steps /3
		LB_SHOULDER.angle = LB_SHOULDER_INIT + theta
		RF_SHOULDER.angle = RF_SHOULDER_INIT - theta
		
		RB_SHOULDER.angle = RB_SHOULDER_INIT - max_deg * step / steps/3
		LF_SHOULDER.angle = LF_SHOULDER_INIT + max_deg * step / steps/3
		x = 51.3 + theta
		y = math.degrees(math.acos(1.58 - math.sin(math.radians(x))/1.26)) + 38.7 - theta
		#print(y)
		delta = 55.2-y
		LB_KNEE.angle = LB_KNEE_INIT -delta
		RF_KNEE.angle = RF_KNEE_INIT +delta
		
		#RB_KNEE.angle = RB_KNEE_INIT + 30 * (1-
		#LF_KNEE.angle = LF_KNEE_INIT -delta
		time.sleep(delay)
	
	RB_KNEE.angle = RB_KNEE_INIT + fwd_deg
	LF_KNEE.angle = LF_KNEE_INIT - fwd_deg
	
	
	time.sleep(1)
	
	
	# RB LF fwd max_deg
	LB_KNEE.angle = LB_KNEE_INIT + alpha
	RF_KNEE.angle = RF_KNEE_INIT - alpha
	
	for step in range(steps*3):
		theta = max_deg - (max_deg-min_deg) * step / steps /3
		RB_SHOULDER.angle = RB_SHOULDER_INIT - theta
		LF_SHOULDER.angle = LF_SHOULDER_INIT + theta
		
		LB_SHOULDER.angle = LB_SHOULDER_INIT + max_deg * step / steps/3
		RF_SHOULDER.angle = RF_SHOULDER_INIT - max_deg * step / steps/3
		x = 51.3 + theta
		y = math.degrees(math.acos(1.58 - math.sin(math.radians(x))/1.26)) + 38.7 - theta
		#print(y)
		delta = 55.2-y
		RB_KNEE.angle = RB_KNEE_INIT +delta
		LF_KNEE.angle = LF_KNEE_INIT -delta
		
		#RB_KNEE.angle = RB_KNEE_INIT + 30 * (1-
		#LF_KNEE.angle = LF_KNEE_INIT -delta
		time.sleep(delay)
	
	LB_KNEE.angle = LB_KNEE_INIT - fwd_deg
	RF_KNEE.angle = RF_KNEE_INIT + fwd_deg
		
		
		
		
		
		
		
		
		
	
	
	'''
	
	for step in range(steps):
    	LB_SHOULDER.angle = LB_SHOULDER_INIT - 5
	    RF_SHOULDER.angle = RF_SHOULDER_INIT + 5
	    LB_KNEE.angle = LB_KNEE_INIT + 30
	    RF_KNEE.angle = RB_KNEE_INIT - 30
	    LB_SHOULDER.angle = LB_SHOULDER_INIT + max_deg
	    RF_SHOULDER.angle = RF_SHOULDER_INIT - max_deg	
	    time.sleep(0.2)
	    LB_KNEE.angle = LB_KNEE_INIT - fwd_deg
	    RF_KNEE.angle = RB_KNEE_INIT + fwd_deg
	'''
	
	
	'''
	for step in range(steps):
		
		
		
	for step in range(steps*3):
		theta = max_deg - (max_deg-min_deg) * step / steps /3
		LB_SHOULDER.angle = LB_SHOULDER_INIT + theta
		RB_SHOULDER.angle = RB_SHOULDER_INIT - theta
		LF_SHOULDER.angle = LF_SHOULDER_INIT + theta
		RF_SHOULDER.angle = RF_SHOULDER_INIT - theta
		x = 51.3 + theta
		y = math.degrees(math.acos(1.58 - math.sin(math.radians(x))/1.26)) + 38.7 - theta
		print(y)
		delta = 55.2-y
		LB_KNEE.angle = LB_KNEE_INIT -delta
		RB_KNEE.angle = RB_KNEE_INIT +delta
		LF_KNEE.angle = LF_KNEE_INIT -delta
		RF_KNEE.angle = RF_KNEE_INIT +delta
		time.sleep(delay)
	'''
	
	'''
	for step in range(steps*3):
		theta = 
		y = math.acos(1.58 - math.sin(x)) + 38.7 + theta
		
		
	for step in range(steps*2):
		theta = 
		y = math.acos(1.58 - math.sin(x)) + 38.7 + theta
	'''
		
	    
    
def main():
    init_spot()
    time.sleep(2)
    floor_test(steps = 20,delay=0.002)
    time.sleep(10)
        
    print("Returning to initial posture...")
    init_spot()
    pca1.deinit()

if __name__ == '__main__':
    main()
	
