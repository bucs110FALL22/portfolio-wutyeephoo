import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

turtle1 = int(random.randrange(1, 101))
turtle2 = int(random.randrange(1, 101))

michelangelo.forward(turtle1)
leonardo.forward(turtle2)

for i in range(10):
  turtle1 = int(random.randrange(1, 101))
  turtle2 = int(random.randrange(1, 101))
  michelangelo.forward(turtle1)
  leonardo.forward(turtle2)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()

coords = []

num_sides = 3
side_length = 50
offset = 100
window.fill("white")

for i in range(num_sides):
  theta = ((2.0 * math.pi * i) / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += [[x,y]]

pygame.draw.polygon(window, "green", coords) 

pygame.display.flip()
pygame.time.wait(5000)

window.fill("white")
pygame.display.flip()

num_sides = 4
coords = []

for i in range(num_sides):
  theta = ((2.0 * math.pi * i) / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += [[x,y]]

pygame.draw.polygon(window, "green", coords) 

pygame.display.flip()
pygame.time.wait(5000)

window.fill("white")
pygame.display.flip()

num_sides = 6
coords = []

for i in range(num_sides):
  theta = ((2.0 * math.pi * i) / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += [[x,y]]

pygame.draw.polygon(window, "green", coords) 

pygame.display.flip()
pygame.time.wait(10000)

window.fill("white")
pygame.display.flip()

num_sides = 9
coords = []

for i in range(num_sides):
  theta = ((2.0 * math.pi * i) / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += [[x,y]]

pygame.draw.polygon(window, "green", coords) 

pygame.display.flip()
pygame.time.wait(10000)

window.fill("white")
pygame.display.flip()

num_sides = 360
coords = []

for i in range(num_sides):
  theta = ((2.0 * math.pi * i) / num_sides)
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords += [[x,y]]

pygame.draw.polygon(window, "green", coords) 

pygame.display.flip()
pygame.time.wait(10000)

window.fill("white")
pygame.display.flip()