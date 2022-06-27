#-------------------------------------
#          <front>
# (0 1 2)          (9 10 11)
# 
#
# (6 7 8)          (3 4 5)
#          <hind>
# motor configuration 
#-------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pcaScenario():
    for i in range(numServo):
        for j in range(MIN_ANG[i],MAX_ANG[i],1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i],MIN_ANG[i],-1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        pca.servo[i].angle=None 
        time.sleep(0.5)

def partialReturn(a):
    pca.servo[a] = 90
    pca.servo[a+1] = 90
    pca.servo[a+2] = 90

def forward():
    for i in range(0,10,3):
        pca.servo[i] = 50
        pca.servo[i+1] = 60
        pca.servo[i+2] = 70
        if i%6==0 :
            partialReturn(i)


