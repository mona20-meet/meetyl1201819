import turtle
from turtle import *
import random

class rfatfts(Turtle):
	def __init__ (self, radius, color, dx, dy, x, y):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.penup()
		self.dx = dx
		self.dy = dy
		self.x = x
		self.y = y 
		self.goto(x,y)


	def Move(self,screen_height,screen_width):
		current_x ,current_y = self.pos()
		newx = current_x + self.dx
		newy = current_y + self.dy
		right_side = newx + self.radius
		left_side = newx -self.radius
		top_side = newy + self.radius
		bottom_side = newy - self.radius

		self.goto(newx, newy)
		if top_side > screen_height or bottom_side < screen_height:
			self.dx = -self.dx
		if top_side < -screen_height or right_side > screen_height:
			self.dy = -self.dy

'''ball1 = Ball(50,'blue',1.5,1.5,23,23)

while 1==1:
	ball1.Move(100,100)'''







turtle.mainloop()