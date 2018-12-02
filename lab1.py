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
turtle.begin_fill()
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
turtle.circle(100)
turtle.penup()
turtle.goto(-50,80)
turtle.pendown()
turtle.circle(120)
turtle.end_fill()
turtle.mainloop()