from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0.00
gravity = 0.01
ay = gravity

power = 0.3

def handle_keydown(key):
  global ax, ay, power
  

  if key == "left":
    ax = -power 
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power
   
  power = power*(1-gravity)
 
def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  
