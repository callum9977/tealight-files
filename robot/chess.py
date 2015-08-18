from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while look() == 'fruit':
    move()
    if right_side() == 'fruit':
      turn(1)
      
move()
turn(1)
while look() == none:
  move()
while look == 'fruit':
  move()
    
