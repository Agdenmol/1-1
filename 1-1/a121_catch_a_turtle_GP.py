# a121_catch_a_turtle.py
import turtle as trtl
spot=trtl.Turtle()
#-----import statements-----
import random as rand

#-----game configuration----
spot_color = "aqua"
spot_size = 2
spot_shape = "circle"
#-----initialize turtle-----
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.speed(0)
spot.penup()
#-----game functions--------
def spot_clicked(x,y):
  change_position() 
def change_position():
  new_xpos = rand.randint(-400, 400)
  new_ypos = rand.randint(-300, 300)
  spot.goto(new_xpos,new_ypos)



#-----events----------------
spot.onclick(spot_clicked)
wn=trtl.Screen()
wn.mainloop()