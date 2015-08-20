from tealight.art import (color, line, spot, circle, box, image, text, background)

for j in range(0,9):
  for i in range(0,9):
    color("blue")
    box(i*60, j*60, 50, 50)
  
