import turtle
x = turtle.Turtle()
color = ["red","green","blue","cyan","magenta","yellow","white"]
x.speed(0)
for i in range(6):
   for a in color:
       x.color(a)
       x.begin_fill()
       x.circle(150)
       x.right(360/42)
x.hideturtle()
turtle.Screen().exitonclick()