import turtle

my_turtle = turtle.Turtle()

num_sides = int(input("Please enter the number of sides: "))
my_turtle.color("purple")
length = 50
angle = 360 / num_sides

# my_turtle.down()

my_turtle.forward(length)
my_turtle.left(angle)
my_turtle.forward(length)
my_turtle.left(angle)
my_turtle.forward(length)
my_turtle.left(angle)
my_turtle.forward(length)
my_turtle.left(angle)

# my_turtle.up()

window.exitonclick()