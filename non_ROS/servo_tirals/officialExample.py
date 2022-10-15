import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 8)

def main():
    kit.servo[0].angle = 180
    kit.continuous_servo[1].throttle = 1
    time.sleep(1)

    kit.continuous_servo[1].throttle = - 1
    time.sleep(1)

    kit.servo[0].angle = 0
    kit.continuous_servo[1].throttle = 0

if __name__ == '__main__':
    main()