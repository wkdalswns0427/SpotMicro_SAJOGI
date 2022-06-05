#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time    
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
import movement as mv

#Constants
numServo=16 
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

pca = ServoKit(channels=16)

def init():
    for i in range(numServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])


def main():
    try:
        while True:
            var = raw_input(" Enter direction (f/b/l/r/d) :")
            if var == 'f':
                for i in range(5):
                    mv.forward()
                    i++1
            elif var == 'b':
                for i in range(5):
                    mv.backward()
                    i++1
            elif var == 'l':
                mv.left_turn()
            elif var == 'r':
                mv.right_turn()
            elif var == 'd':
                mv.pcaScenario()
            else:
                print("Statement Error")
                

if __name__ == '__main__':
    init()
    main()
