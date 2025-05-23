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
shoulder2 = 52
knee2 = 40

RF_KNEE_INIT     = 65 + knee2
RF_SHOULDER_INIT = 51 + shoulder2
RF_HIP_INIT      = 83

RB_KNEE_INIT     = 76 + knee2
RB_SHOULDER_INIT = 56.2 + shoulder2
RB_HIP_INIT      = 87

LF_KNEE_INIT     = 98 - knee2
LF_SHOULDER_INIT = 118 - shoulder2
LF_HIP_INIT      = 94

LB_KNEE_INIT     = 117 - knee2
LB_SHOULDER_INIT = 92.5 - shoulder2
LB_HIP_INIT      = 84

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

# 초기 자세
def init_spot():
    RF_KNEE.angle, RF_SHOULDER.angle = RF_KNEE_INIT, RF_SHOULDER_INIT
    RB_KNEE.angle, RB_SHOULDER.angle = RB_KNEE_INIT, RB_SHOULDER_INIT
    LF_KNEE.angle, LF_SHOULDER.angle = LF_KNEE_INIT, LF_SHOULDER_INIT
    LB_KNEE.angle, LB_SHOULDER.angle = LB_KNEE_INIT, LB_SHOULDER_INIT
    time.sleep(0.5)

# 앞으로 걷기
def trot_step_forward(steps=40, delay=0.001):
    knee_amp = -15
    shoulder_amp = 17

    for step in range(steps):
        phase = 2 * math.pi * step / (steps - 1)

        base = math.sin(phase)
        base_opp = math.sin(phase + math.pi)

        knee_flex = (1 - math.cos(phase)) / 2
        knee_flex_opp = (1 - math.cos(phase + math.pi)) / 2

        LF_SHOULDER.angle = LF_SHOULDER_INIT + shoulder_amp * base
        time.sleep(delay)
        LF_KNEE.angle = LF_KNEE_INIT - knee_amp * knee_flex
        time.sleep(delay)

        LB_SHOULDER.angle = LB_SHOULDER_INIT + shoulder_amp * base_opp
        time.sleep(delay)
        LB_KNEE.angle = LB_KNEE_INIT - knee_amp * knee_flex_opp
        time.sleep(delay)

        RF_SHOULDER.angle = RF_SHOULDER_INIT - shoulder_amp * base_opp
        time.sleep(delay)
        RF_KNEE.angle = RF_KNEE_INIT + knee_amp * knee_flex_opp
        time.sleep(delay)

        RB_SHOULDER.angle = RB_SHOULDER_INIT - shoulder_amp * base
        time.sleep(delay)
        RB_KNEE.angle = RB_KNEE_INIT + knee_amp * knee_fleximport time
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
shoulder2 = 52
knee2 = 40

RF_KNEE_INIT     = 65 + knee2
RF_SHOULDER_INIT = 51 + shoulder2
RF_HIP_INIT      = 83

RB_KNEE_INIT     = 76 + knee2
RB_SHOULDER_INIT = 56.2 + shoulder2
RB_HIP_INIT      = 87

LF_KNEE_INIT     = 98 - knee2
LF_SHOULDER_INIT = 118 - shoulder2
LF_HIP_INIT      = 94

LB_KNEE_INIT     = 117 - knee2
LB_SHOULDER_INIT = 92.5 - shoulder2
LB_HIP_INIT      = 84

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

# 초기 자세
def init_spot():
    RF_KNEE.angle, RF_SHOULDER.angle = RF_KNEE_INIT, RF_SHOULDER_INIT
    RB_KNEE.angle, RB_SHOULDER.angle = RB_KNEE_INIT, RB_SHOULDER_INIT
    LF_KNEE.angle, LF_SHOULDER.angle = LF_KNEE_INIT, LF_SHOULDER_INIT
    LB_KNEE.angle, LB_SHOULDER.angle = LB_KNEE_INIT, LB_SHOULDER_INIT
    time.sleep(0.5)

# 앞으로 걷기
def trot_step_forward(steps=40, delay=0.001):
    knee_amp = -15
    shoulder_amp = 17

    for step in range(steps):
        phase = 2 * math.pi * step / (steps - 1)

        base = math.sin(phase)
        base_opp = math.sin(phase + math.pi)

        knee_flex = (1 - math.cos(phase)) / 2
        knee_flex_opp = (1 - math.cos(phase + math.pi)) / 2

        LF_SHOULDER.angle = LF_SHOULDER_INIT + shoulder_amp * base
        time.sleep(delay)
        LF_KNEE.angle = LF_KNEE_INIT - knee_amp * knee_flex
        time.sleep(delay)

        LB_SHOULDER.angle = LB_SHOULDER_INIT + shoulder_amp * base_opp
        time.sleep(delay)
        LB_KNEE.angle = LB_KNEE_INIT - knee_amp * knee_flex_opp
        time.sleep(delay)

        RF_SHOULDER.angle = RF_SHOULDER_INIT - shoulder_amp * base_opp
        time.sleep(delay)
        RF_KNEE.angle = RF_KNEE_INIT + knee_amp * knee_flex_opp
        time.sleep(delay)

        RB_SHOULDER.angle = RB_SHOULDER_INIT - shoulder_amp * base
        time.sleep(delay)
        RB_KNEE.angle = RB_KNEE_INIT + knee_amp * knee_flex
        time.sleep(delay)

    LF_SHOULDER.angle = LF_SHOULDER_INIT
    LF_KNEE.angle = LF_KNEE_INIT - knee_amp * knee_flex
    LB_SHOULDER.angle = LB_SHOULDER_INIT
    LB_KNEE.angle = LB_KNEE_INIT - knee_amp * knee_flex_opp
    RF_SHOULDER.angle = RF_SHOULDER_INIT
    RF_KNEE.angle = RF_KNEE_INIT + knee_amp * knee_flex_opp
    RB_SHOULDER.angle = RB_SHOULDER_INIT
    RB_KNEE.angle = RB_KNEE_INIT + knee_amp * knee_flex
    time.sleep(delay)

# 뒤로 걷기
def trot_step_backward(steps=40, delay=0.002):
    knee_amp = -15
    shoulder_amp = 17

    for step in range(steps,0,-1):
        phase = 2 * math.pi * step / (steps - 1)

        base = math.sin(phase + math.pi)
        base_opp = math.sin(phase)

        knee_flex = (1 - math.cos(phase)) / 2
        knee_flex_opp = (1 - math.cos(phase + math.pi)) / 2

        LF_SHOULDER.angle = LF_SHOULDER_INIT + shoulder_amp * base
        time.sleep(delay)
        LF_KNEE.angle = LF_KNEE_INIT - knee_amp * knee_flex
        time.sleep(delay)

        LB_SHOULDER.angle = LB_SHOULDER_INIT + shoulder_amp * base_opp
        time.sleep(delay)
        LB_KNEE.angle = LB_KNEE_INIT - knee_amp * knee_flex_opp
        time.sleep(delay)

        RF_SHOULDER.angle = RF_SHOULDER_INIT - shoulder_amp * base_opp
        time.sleep(delay)
        RF_KNEE.angle = RF_KNEE_INIT + knee_amp * knee_flex_opp
        time.sleep(delay)

        RB_SHOULDER.angle = RB_SHOULDER_INIT - shoulder_amp * base
        time.sleep(delay)
        RB_KNEE.angle = RB_KNEE_INIT + knee_amp * knee_flex
        time.sleep(delay)

    LF_SHOULDER.angle = LF_SHOULDER_INIT
    LF_KNEE.angle = LF_KNEE_INIT - knee_amp * knee_flex
    LB_SHOULDER.angle = LB_SHOULDER_INIT
    LB_KNEE.angle = LB_KNEE_INIT - knee_amp * knee_flex_opp
    RF_SHOULDER.angle = RF_SHOULDER_INIT
    RF_KNEE.angle = RF_KNEE_INIT + knee_amp * knee_flex_opp
    RB_SHOULDER.angle = RB_SHOULDER_INIT
    RB_KNEE.angle = RB_KNEE_INIT + knee_amp * knee_flex
    time.sleep(delay)

# 메인 루프
def main():
    init_spot()
    time.sleep(1)

    for i in range(5):  # 앞뒤 걷기 5번 반복 (총 10번 움직임)
        print(f"Step {i+1}: Forward")
        trot_step_forward()
        time.sleep(0.5)

        print(f"Step {i+1}: Backward")
        trot_step_backward()
        time.sleep(0.5)

    print("Returning to initial posture...")
    init_spot()
    pca1.deinit()

if __name__ == "__main__":
    main()
