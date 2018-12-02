import turtle
image = 'yes.gif'
turtle.addshape(image)
turtle.shape(image)
turtle.speed(40)
for i in range (360) :
	turtle.forward(170)
	turtle.right(45)
	turtle.forward(75)
	turtle.right(95)
	turtle.forward(35)
	turtle.penup()
	turtle.goto(0,0)
	turtle.pendown()
	turtle.right(0.6)

turtle.mainloop()
#lab_is_finished