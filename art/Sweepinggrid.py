import random
from random import randrange
from math import floor
from tealight.art import (color, line, spot, circle, box, image, text, background)
color('white')
box(0,0,1000,1000)
score = 0

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
  position = (11*(y))+x
  return A[position]
 
#this sets the information about a box to the corresponding lis
def setbox(A, x, y, val):
  position = (11*(y))+x
  A[position] = val
 
#Determines numbers
def getSurroundingMines(x, y):
  surround = 0
  global mine
  for i in range(-1,2):
    for j in range(-1, 2):
      surround=surround+get(mine, x+i, y+j)
  color('black')
  if surround>0:
    text(x*60 + 17, y*60 + 20 , surround)
  return surround
 
#this finds which box is clicked
def handle_mousedown(x, y):
  global score
  boxX = floor(x/60)
  boxY = floor(y/60)
  print boxY, boxX
  print get(mine, boxX, boxY)
  if get(mine, boxX, boxY)==1:
    color('red')
    box(boxX*60,boxY*60,50,50)
  if get(mine, boxX, boxY)==0:
    color('white')
    box(boxX*60,boxY*60,50,50)
    print getSurroundingMines(boxX,boxY)
    score = score+1
    print(score)
    text(50,700, score)
    
   
 
 
#this is where the program starts
makegrid()
 
mine = []
for i in range(0, 121):
  mine.append(0)
 
for i in range(0,15):
  b=0
  while b==0:
    x=randrange(0,9,1)
    y=randrange(0,9,1)
    if get(mine, x, y) == 0:
      setbox(mine,x,y,1)
      b=1