import turtle
my_turtle = turtle.Turtle()
screen = turtle.Screen()
sides = int(input("Enter the number of sides: "))

length = int(input("Enter the length: "))

my_turtle.color("purple")
#color that the turtle will use

angle = ( 360 / sides )

for i in [angle]*sides:
	my_turtle.left(angle)
	my_turtle.forward(length)

screen.exitonclick()