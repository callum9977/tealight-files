from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

for n in range(0,distance):
  if look() == 'fruit':
    move()  