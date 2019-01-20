import turtle
from turtle import *
import random

class Ball(Turtle):
	def __init__ (self, radius, color, dx, dy, x, y):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.penup()
		self.speed(0)
		self.dx = dx
		self.dy = dy
		self.goto(x,y)


	def Move (self, screen_width, screen_height):
		self.screen_width = 5000
		self.screen_height = 5000
		oldx = self.xcor()
		oldy = self.ycor()
		newx = oldx + self.dx
		newy = oldy + self.dy
		right_side = newx + self.radius
		left_side = newx + self.radius
		top_side = newy + self.radius
		bottom_side = newy + self.radius

		self.goto(newx, newy)
		if top_side > screen_height or bottom_side < screen_height:
			self.dx *= -1
		if top_side < -screen_height or right_side > screen_height:
			self.dy *= -1

ball1 = Ball(50,'blue',23,23,23,23)

ball2 = Ball(40,'purple',23,23,23,23)










turtle.mainloop()