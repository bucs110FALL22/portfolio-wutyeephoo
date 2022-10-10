import turtle
import random

def isinscreen(window, turt):
  turtleX = turt.xcor()
  turtleY = turt.ycor()

  x_range = window.window_width()/2
  y_range = window.window_height()/2
  if abs(turtleX) > x_range or abs(turtleY) > y_range:
    return False
  return True

window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.speed(0)

distance = 10
angle = 90
is_in_screen = True

colors = ["green", "blue", "purple"]

while isinscreen(window, my_turtle):
  coin = random.randrange(0, 2)
  if coin:
    my_turtle.right(angle)
  else:
    my_turtle.left(angle)
  my_turtle.forward(distance)
  my_turtle.color(colors[0])

  colors.append(colors.pop(0))

window.bgcolor("blue")
window.exitonclick()