class Animal(object):
	def __init__(self,name,age,favfood):
		self.name = name
		self.favfood = favfood
	def eat(self,food):
		print(self.name + 'is eating' + food)
	def description(self):
		print(self.name + 'is'+ age + 'years old' + 'is eating' + self.favfood)
s = Animal('nour',2,'chocolate')
description()
