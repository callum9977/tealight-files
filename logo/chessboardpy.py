from tealight.logo import move, turn
def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)

def line_squares(number,size):
  for i in range(number):
    polygon(4,size)
    turn(90)
    move(size)
    turn(-90)
line_squares(8,30)