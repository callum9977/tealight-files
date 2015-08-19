from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 150

width = 20
height = 8

for i in range(0,width):
  for j in range(0,height):
    if i % 4 == 0:
      image(10 * 60, 10 * 40, "misc/YellowFlower.png")
    else:
      image(x + i * 60, y + i * 40, "misc/Clover.png")
     
