from turtle import *
import turtle
from turtle import Turtle
import random
'''
turtle.colormode(255)
class square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape('square')
	def random_color(self):
		r=random.randint(0,256)
		b=random.randint(0,256)
		g=random.randint(0,256)
		self.color(r,b,g)
turtle1= square(10)
turtle1.random_color()
turtle.mainloop()

class hexagon(Turtle):
'''
turtle.home()
for i in range (6):
	turtle.begin_poly()
	turtle.fd(100)
	turtle.left(60)

	turtle.end_poly()
yeet= turtle.get_poly()
register_shape('yeet', yeet)
turtle.mainloop()
#lab_is_finished