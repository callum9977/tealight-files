import random

from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
n=0
while n<2000:
  n = n+1
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
  elif:
    while smell() >= 1:
      i = random.randint (-1, 2)
      turn(i)
      move()
  else:
    i = random.randint (-1, 2)
      turn(i)
      move()
