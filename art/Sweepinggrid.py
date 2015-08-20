import random
from random import randrange
from math import floor
from tealight.art import (color, line, spot, circle, box, image, text, background)
 
 
#this makes the grid
def makegrid():
  for j in range(0, 10):
    for i in range(0, 10):
      if((i+j) % 2) !=1:
        color("black")
      else:
        color("blue")
      box(i*60, j*60, 50, 50)
 
#this gets the information about a box from the corresponding list
def get(A, x, y):
  position = (10*(y))+x
  return A[position]
 
#this sets the information about a box to the corresponding lis
def setbox(A, x, y, val):
  position = (10*(y))+x
  A[position] = val
 
#this ffinds which box is clicked
def handle_mousedown(x, y):
  boxX = floor(x/60)
  boxY = floor(y/60)
  print boxY, boxX
  print get(mine, boxX, boxY)
 
 
#this is where the program starts
makegrid()
 
mine = []
for i in range(0, 100):
  mine.append(0)
 
for i in range(0,15):
  x=randrange(0,9,1)
  y=randrange(0,9,1)
  setbox(mine,x,y,1)