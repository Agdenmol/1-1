#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 8
y = 70
leg_rotation = 380 / legs
print("leg_rotation=", leg_rotation)
spider.pensize(5)
n = 0
while (n < legs):
  print("leg_rotation*n=", leg_rotation*n)
  spider.goto(0,0)
  spider.setheading(leg_rotation*n)
  spider.forward(y)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()