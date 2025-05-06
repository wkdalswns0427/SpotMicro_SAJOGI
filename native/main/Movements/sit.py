import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# I2C와 PCA9685 설정
i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60

# 서보 핀 번호
LF_KNEE_PIN, LF_SHOULDER_PIN, LF_HIP_PIN = 10, 9, 8
LB_KNEE_PIN, LB_SHOULDER_PIN, LB_HIP_PIN = 2, 1, 0
RF_KNEE_PIN, RF_SHOULDER_PIN, RF_HIP_PIN = 14, 13, 12
RB_KNEE_PIN, RB_SHOULDER_PIN, RB_HIP_PIN = 6, 5, 4

# 초기 각도 설정
'''
RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT = 90, 140, 80
RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT = 93, 150, 90
LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT = 70, 30, 90
LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT = 90, 45, 90
'''


shoulder2 = 71
knee2	 = 10

RF_KNEE_INIT     =           65   + knee2    # small down  
RF_SHOULDER_INIT =           51   +shoulder2    #small down 
RF_HIP_INIT      =           83 

RB_KNEE_INIT     =           76   +knee2
RB_SHOULDER_INIT =           56.2   +shoulder2    # small down
RB_HIP_INIT      =           87

LF_KNEE_INIT     =           98    -knee2    # small up 
LF_SHOULDER_INIT =           118   -shoulder2       # small downS
LF_HIP_INIT      =           94


LB_KNEE_INIT     =           117     -knee2     # small up 
LB_SHOULDER_INIT =           92.5   -shoulder2
LB_HIP_INIT      =           84

# 서보 객체 생성
RF_KNEE = servo.Servo(pca1.channels[RF_KNEE_PIN])
RF_SHOULDER = servo.Servo(pca1.channels[RF_SHOULDER_PIN])
RF_HIP = servo.Servo(pca1.channels[RF_HIP_PIN])

RB_KNEE = servo.Servo(pca1.channels[RB_KNEE_PIN])
RB_SHOULDER = servo.Servo(pca1.channels[RB_SHOULDER_PIN])
RB_HIP = servo.Servo(pca1.channels[RB_HIP_PIN])

LF_KNEE = servo.Servo(pca1.channels[LF_KNEE_PIN])
LF_SHOULDER = servo.Servo(pca1.channels[LF_SHOULDER_PIN])
LF_HIP = servo.Servo(pca1.channels[LF_HIP_PIN])

LB_KNEE = servo.Servo(pca1.channels[LB_KNEE_PIN])
LB_SHOULDER = servo.Servo(pca1.channels[LB_SHOULDER_PIN])
LB_HIP = servo.Servo(pca1.channels[LB_HIP_PIN])


# 초기 자세로 설정하는 함수
def init_spot():
    print("Initializing to default posture...")
    RF_KNEE.angle, RF_SHOULDER.angle, RF_HIP.angle = RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT
    RB_KNEE.angle, RB_SHOULDER.angle, RB_HIP.angle = RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT
    LF_KNEE.angle, LF_SHOULDER.angle, LF_HIP.angle = LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT
    LB_KNEE.angle, LB_SHOULDER.angle, LB_HIP.angle = LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT
    time.sleep(0.5) 


# 천천히 무릎과 어깨를 움직이는 함수
def smooth_move(knee_offsets, shoulder_offsets, steps=20, delay=0.05):
    # 현재 무릎과 어깨 각도 저장
    start_knees = [RF_KNEE.angle, RB_KNEE.angle, LF_KNEE.angle, LB_KNEE.angle]
    start_shoulders = [RF_SHOULDER.angle, RB_SHOULDER.angle, LF_SHOULDER.angle, LB_SHOULDER.angle]

    # 목표 각도 계산
    target_knees = [start + offset for start, offset in zip(start_knees, knee_offsets)]
    target_shoulders = [start + offset for start, offset in zip(start_shoulders, shoulder_offsets)]

    for step in range(steps + 1):
        ratio = step / steps

        # 무릎 업데이트
        RF_KNEE.angle = start_knees[0] + (target_knees[0] - start_knees[0]) * ratio
        RB_KNEE.angle = start_knees[1] + (target_knees[1] - start_knees[1]) * ratio
        LF_KNEE.angle = start_knees[2] + (target_knees[2] - start_knees[2]) * ratio
        LB_KNEE.angle = start_knees[3] + (target_knees[3] - start_knees[3]) * ratio

        # 어깨 업데이트
        RF_SHOULDER.angle = start_shoulders[0] + (target_shoulders[0] - start_shoulders[0]) * ratio
        RB_SHOULDER.angle = start_shoulders[1] + (target_shoulders[1] - start_shoulders[1]) * ratio
        LF_SHOULDER.angle = start_shoulders[2] + (target_shoulders[2] - start_shoulders[2]) * ratio
        LB_SHOULDER.angle = start_shoulders[3] + (target_shoulders[3] - start_shoulders[3]) * ratio

        time.sleep(delay)

knee = 65
shoulder = 19


# 천천히 앉는 함수
def sit_spot():
    print("Sitting down slowly...")
    smooth_move(
        knee_offsets = (-knee, -knee, knee, knee),     # 무릎 각도 변화량
        shoulder_offsets = (shoulder, shoulder, -shoulder, -shoulder), # 어깨 각도 변화량
        steps = 30,
        delay = 0.01
    )


# 천천히 일어나는 함수
def stand_spot():
    print("Standing up slowly...")
    smooth_move(
        knee_offsets = (knee, knee, -knee, -knee),     # 무릎을 원래로 복귀
        shoulder_offsets = (-shoulder, -shoulder, shoulder, shoulder), # 어깨도 원래로 복귀
        steps = 30,
        delay = 0.01
    )


# 메인 함수
def main():
    init_spot()
    time.sleep(1)

    for _ in range(3):  # 3번 반복
        sit_spot()
        time.sleep(1.0)
        stand_spot()
        time.sleep(1.0)

    pca1.deinit()  # I2C 장치 해제


if __name__ == '__main__':
    main()
