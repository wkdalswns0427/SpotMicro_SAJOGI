#-------------------------------------
#          <front>
# (0 1 2)          (9 10 11)
# 
#
# (6 7 8)          (3 4 5)
#          <hind>
# motor configuration 
#-------------------------------------

# forward movement
def move_forward():
  try:
    servo0.angle = 55
    servo1.angle = 70
    servo2.angle = 70  
    servo1.angle = 90
    servo2.angle = 90  
    
    servo3.angle = 55
    servo4.angle = 70
    servo5.angle = 70 
    servo4.angle = 90
    servo5.angle = 90 
    
    time.sleep(10)
    
    servo6.angle = 55
    servo7.angle = 70
    servo8.angle = 70  
    servo7.angle = 90
    servo8.angle = 90  
  
    servo9.angle = 55
    servo10.angle = 70
    servo11.angle = 70   
    servo10.angle = 90
    servo11.angle = 90  
    
    time.sleep(10)
    
  except KeyboardInterrupt
    print("exit all motion")
 
  
  
