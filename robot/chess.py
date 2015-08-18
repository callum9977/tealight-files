from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while look() == 'fruit':
    move()
    
turn(1)

while look() == 'fruit':
    move()
    
while look() == 'fruit':
    move()
    
turn(1)

while look() == 'fruit':
    move()
    
turn(1)

while look() == 'fruit':
    move()
    
turn(1)