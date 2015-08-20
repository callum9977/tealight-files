import random
from random import randrange
from math import floor
from tealight.art import (color, line, spot, circle, box, image, text, background)
score=0
ingame=1
color('white')
box(0,0,1000,1000)
color("black")
text(0, 600,"Score: "+str(score))
 
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
      if get(mine, x+i, y+j) ==1:
        surround=surround+1
  color('black')
  if surround>0:
    text(x*60 + 17, y*60 + 20 , surround)
  return surround
 
#this finds which box is clicked
def handle_mousedown(x, y,button):
 
  global score
  boxX = floor(x/60)
  boxY = floor(y/60)
  if boxX<10:
    if boxY<10:
      if ingame == 1:
        if button=="left":
          uncover(boxX, boxY)
        if button=="right"and get(mine, boxX, boxY)!=2:
          color("green")
          spot(boxX*60 +25 ,boxY*60 + 25,10)
 
def uncover(boxX, boxY):
  global score
  global ingame
  global mine
  print boxY, boxX
  print get(mine, boxX, boxY)
  if get(mine, boxX, boxY)==1:
    color('red')
    box(boxX*60,boxY*60,50,50)
    ingame=0
    color("white")
    box(0,600,500,50)
    color("black")
    text(0, 600,"Final score: "+str(score))
    text(500,600, "You Lost!")
  if get(mine, boxX, boxY)==0:
    color('white')
    box(boxX*60,boxY*60,50,50)
    setbox(mine,boxX,boxY,2)
    end =  getSurroundingMines(boxX,boxY)
    score+=1
    color("white")
    box(0,600,500,50)
    color("black")
    text(0, 600,"Score: "+str(score))
    if score==93:
      ingame=0
      box(0,600,500,50)
      color("black")
      text(0, 600,"Final score: "+str(score))
      text(500,600, "You WIN!")
    if end == 0:
      if boxX<9:
        if boxY<9:
          if boxX>0:
            if boxY>0:
              uncover(boxX +1, boxY)
              uncover(boxX -1, boxY)
              uncover(boxX, boxY +1)
              uncover(boxX, boxY -1)
      if boxX<9:
        if boxY==9:
          if boxX>0:
            uncover(boxX +1, boxY)
            uncover(boxX -1, boxY)
            uncover(boxX, boxY -1)
      if boxX<9:
        if boxY==0:
          if boxX>0:
            uncover(boxX +1, boxY)
            uncover(boxX -1, boxY)
            uncover(boxX, boxY +1)
      if boxY<9:
        if boxX==9:
          if boxY>0:
            uncover(boxX +1, boxY)
            uncover(boxX -1, boxY)
            uncover(boxX, boxY -1)
      if boxY<9:
        if boxX==0:
          if boxY>0:
            uncover(boxX, boxY +1)
            uncover(boxX, boxY -1)
            uncover(boxX +1, boxY)
      if boxX == 0:
        if boxY == 9:
          uncover(boxX, boxY -1)
          uncover(boxX +1, boxY)
      if boxX == 9:
        if boxY == 0:
          uncover(boxX, boxY +1)
          uncover(boxX -1, boxY)
      if boxX == 0:
        if boxY == 0:
          uncover(boxX, boxY +1)
          uncover(boxX +1, boxY)
      if boxX == 9:
        if boxY == 9:
          uncover(boxX, boxY -1)
          uncover(boxX -1, boxY)
 
 
color('black')
 
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