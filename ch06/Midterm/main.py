import turtle
window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("grey")


def face(myturtle=None):
    myturtle.fillcolor("grey")
    myturtle.begin_fill()
    myturtle.circle(50, 360)
    myturtle.end_fill()

face(my_turtle)

def ears(myturtle=None, side_length=50, num_sides=3):
  my_turtle.up()

  myturtle.setpos(25, 70)
  my_turtle.down()
  
  myturtle.begin_fill()
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.left(360/num_sides)
  myturtle.end_fill()
  
ears(my_turtle)

def ears(myturtle=None, side_length=50, num_sides=3):
  my_turtle.up()

  myturtle.setpos(-75, 70)
  my_turtle.down()

  myturtle.begin_fill()
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.left(360/num_sides)
  myturtle.end_fill()
  
ears(my_turtle)


def eyes(myturtle=None):
  my_turtle.up()

  myturtle.setpos(-15, 50)
  my_turtle.down()
  
  my_turtle.color("black")
  
  myturtle.begin_fill()
  myturtle.circle(5, 360)
  myturtle.end_fill()

eyes(my_turtle)

def eyes(myturtle=None):
  my_turtle.up()
  
  myturtle.setpos(15, 50)
  my_turtle.down()
  my_turtle.color("black")

  myturtle.begin_fill()
  myturtle.circle(5, 360)
  myturtle.end_fill()

eyes(my_turtle)


def nose(myturtle=None, side_length=20, num_sides=3):
  my_turtle.up()
  
  myturtle.setpos(-10, 45)
  my_turtle.down()
  my_turtle.color("beige")

  myturtle.begin_fill()
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.right(360/num_sides)
  myturtle.end_fill()
  
nose(my_turtle)


def teeth(myturtle=None):
  my_turtle.up()
  
  myturtle.setpos(-7, 10)
  my_turtle.down()
  my_turtle.color("black")

  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)
  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)

  myturtle.fillcolor("white")
  myturtle.begin_fill()
  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)
  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)
  myturtle.end_fill()

teeth(my_turtle)

def teeth(myturtle=None):
  my_turtle.up()
  
  myturtle.setpos(4.1, 10)
  my_turtle.down()
  my_turtle.color("black")
  
  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)
  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)

  myturtle.fillcolor("white")
  myturtle.begin_fill()
  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)
  myturtle.forward(10)
  myturtle.left(90)
  myturtle.forward(15)
  myturtle.left(90)
  myturtle.end_fill()

teeth(my_turtle)

window.exitonclick()