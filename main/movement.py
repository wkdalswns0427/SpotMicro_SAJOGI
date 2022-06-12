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
    servo1.angle = 80
    servo2.angle = 100
    servo3.angle = 90
    servo4.angle = 100
    servo5.angle = 100
    servo6.angle = 90
    servo7.angle = 90
    servo8.angle = 80
    servo9.angle = 90
    servo10.angle = 90
    servo11.angle = 80

  def move_forward(self):
    display.lcd_clear()   
    display.lcd_display_string("Move Forward")

    servo7.angle = 50 
    servo10.angle = 60
    time.sleep(0.3)
    servo1.angle =  110
    servo4.angle = 110
    time.sleep(0.3)
    servo4.angle = 160
    servo1.angle =  120
    servo0.angle = 70
    servo3.angle = 120

    time.sleep(10)
  
  def turn_left(self):
    display.lcd_clear()   
    display.lcd_display_string("turn left")
  
  def turn_right(self):
    display.lcd_clear()   
    display.lcd_display_string("turn right")

  def sit_one(self):
    display.lcd_clear()   
    display.lcd_display_string("Spotty sit1")
    servo3.angle = 60
    servo9.angle = 120
    time.sleep(0.3)
    servo0.angle = 50
    servo6.angle = 130
    time.sleep(0.3)
    servo4.angle = 65
    servo10.angle = 115
    time.sleep(0.3)
    
 def sit_two(self):
    display.lcd_clear()   
    display.lcd_display_string("Spotty sit2")
    servo4.angle = 65
    servo10.angle = 115
    servo0.angle = 125
    servo6.angle = 55
    time.sleep(0.2)
    servo1.angle = 115
    servo7.angle = 65
    servo3.angle = 65
    servo9.angle = 115
    time.sleep(0.3)
