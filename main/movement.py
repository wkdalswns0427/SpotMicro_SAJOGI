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
class movement:
  def return_initial(self):
    display.lcd_clear()   
    display.lcd_display_string("Initial State")

    servo0.angle = 90
    servo1.angle = 90
    servo2.angle = 90
    servo3.angle = 90
    servo4.angle = 90
    servo5.angle = 90
    servo6.angle = 90
    servo7.angle = 90
    servo8.angle = 90
    servo9.angle = 90
    servo10.angle = 90
    servo11.angle = 90
    print("spotty return to initial state!")  

  def move_forward(self):
    display.lcd_clear()   
    display.lcd_display_string("Move Forward")

    servo0.angle = 55
    servo1.angle = 70
    servo2.angle = 70  
  
    servo3.angle = 55
    servo4.angle = 70
    servo5.angle = 70 

    servo1.angle = 90
    servo2.angle = 90 

    servo6.angle = 55
    servo7.angle = 70
    servo8.angle = 70  
    
    servo4.angle = 90
    servo5.angle = 90 
    
    servo9.angle = 55
    servo10.angle = 70
    servo11.angle = 70   

    servo7.angle = 90
    servo8.angle = 90  
    
    servo10.angle = 90
    servo11.angle = 90  
      
    time.sleep(10)
  
  def turn_left(self):
    display.lcd_clear()   
    display.lcd_display_string("turn left")
  
  def turn_right(self):
    display.lcd_clear()   
    display.lcd_display_string("turn right")

  def sit(self):
    display.lcd_clear()   
    display.lcd_display_string("Spotty sit")