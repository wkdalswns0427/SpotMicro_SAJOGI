# basic move from adafruit official
# 2022.05.06 / minjun last modified

import time
import Adafruit_PCA9685

robot_handle=Adafruit_PCA9685.PCA9685()
servoMIN = 150
servoMAX = 550
count = 0

def map(value, min_ang, max_ang, min_pulse, max_pulse):
    angle_range = max_ang - min_ang
    pulse_range = max_pulse - min_pulse
    scale_factor = float(angle_range)/float(pulse_range)
    return min_pulse + (value/scale_factor)

def set_angle(channel, angle):
    pulse = int(map(angle, 0, 180, servoMIN, servoMAX))
    robot_handle.set_pwm(cahnnel, 0, pulse)

robot_handle.set_pwm_freq(50)

while True:
    set_angle(0, 10)
    set_angle(1, 100)
    time.sleep(1)
    set_angle(0, 100)
    set_angle(1, 10)
    time.sleep(1)
    print(count)
    count = count + 1
