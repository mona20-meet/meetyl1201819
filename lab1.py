'''
print('mona')
print(' mona'*3)
for i in range (100):
	print(' mona')

'''
'''
number1 = 10
print(number1)
number2= number1/2
print(number2)
'''
'''
list1=[1,52343,3]

for index in list1:
	print(index)
for index in list1:
	print(index)
	print(index*2)
print(list1[0]+list1[1]+list1[2])

'''
'''
import turtle
#turtle.goto(100,100)
turtle.begin_fill()
for i in range (4):
	turtle.forward(100)
	turtle.right(90)
turtle.end_fill()
turtle.mainloop()
'''
import turtle
turtle.speed(40)
turtle.pensize(21)
turtle.penup()
turtle.color('blue')
turtle.goto(-50,100)
turtle.pendown()
turtle.circle(100)
turtle.penup()

turtle.color('black')
turtle.goto(200,100)
turtle.pendown()
turtle.circle(100)
turtle.penup()

turtle.color('red')
turtle.goto(450,100)
turtle.pendown()
turtle.circle(100)
turtle.penup()

turtle.color('yellow')
turtle.goto(75,-20)
turtle.pendown()
turtle.circle(100)
turtle.penup()

turtle.color('green')
turtle.goto(325,-20)
turtle.pendown()
turtle.circle(100)
turtle.penup()



turtle.mainloop()