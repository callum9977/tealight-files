from tealight.art import (color, line, spot, circle, box, image, text, background)

for j in range(0,10):
  for i in range(0,10):
    box(i*60, j*60, 50, 50)
    if ((i+(1+j)) % 2) == 0:
      color("black")
    else:
      color("white")
    
  
