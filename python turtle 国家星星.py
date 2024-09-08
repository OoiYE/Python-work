import turtle
x = turtle.Turtle()
x.color("red","yellow")
x.begin_fill()
x.right(85)
for i in range(13):
   x.forward(50)
   x.left(160)
   x.forward(50)
   x.right(132.5)
x.end_fill()
x.hideturtle()
turtle.Screen().exitonclick()