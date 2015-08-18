from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
while True:
  if look() == 'fruit':
    move()
  elif right_side() == 'fruit':
      turn(1)
      while look() == 'fruit':
        move()
  elif left_side() == 'fruit':
      turn(1)
      while look() == 'fruit':
        move()
  else:
    turn(1)
    move()