from tealight.art import (color, line, spot, circle, box, image, text, background)

for j in range(0,10):
  for i in range(0,10):
     if ((i+j) % 2) != 1:
      color("black")
     else:
      color("blue")
     box(i*60, j*60, 50, 50)
    
    
  
