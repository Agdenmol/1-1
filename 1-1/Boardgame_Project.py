import turtle as trtl

painter = trtl.Turtle()

painter.penup()
painter.setposition(-200,200)
painter.pendown()

x = 0
z = 0


while x > 4:
  while z > 11:
    painter.forward(18)
    painter.right(90)
    painter.forward(18)
    painter.right(90)
    painter.forward(18)
    painter.right(90)
    painter.forward(18)
    painter.right(90)
    painter.forward(20)
   
    x = x + 1
    z = z + 1
  painter.right(90)

wn = trtl.Screen()
wn.mainloop()

