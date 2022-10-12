import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")

num_sides = int(input("Please enter the number of sides for the shape: "))
side_length = int(input("Please enter the side length: "))

def drawEqShape(myturtle=None, side_length=0, num_sides=0):
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.left(360/num_sides)

drawEqShape(my_turtle, side_length, num_sides)