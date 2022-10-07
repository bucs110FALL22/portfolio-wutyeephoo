import turtle
import random

window.bgcolor('lightblue')

pygame.init()
window = pygame.display.set_mode()

window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.goto(100, 50)

coin = ["head","tail"]
chance = random.choice(coin)

coords = []
offset = 100
x, y = my_turtle.pos()
while abs(x) < window.window_width/2:
  if chance == "head":
    my_turtle.left(90)
    my_turtle.forward(50)
  elif chance == "tail":
    my_turtle.left(90)
    my_turtle.forward(50)

window.exitonclick()