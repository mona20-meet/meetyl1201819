class Animal(object):
	def __init__(self,name,age,favfood,sound):
		self.name = name
		self.favfood = favfood
		self.age=age
		self.sound=sound
	def eat(self,food):
		print(self.name + ' is eating ' + food)
	def description(self):
		print(self.name + ' is '+ self.age + ' years old ' + ' and is eating ' + self.favfood)
	def make_sound(self):
		print(self.name +':'+ self.sound *3)
s = Animal('nour','2','chocolate',' bark')
s.description()
s.eat('strawberries')
s.make_sound()
class Person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat_fav_breakfast(self, fav_breakfast):
		print(self.name + ' is eating '+ fav_breakfast)
	def play_sport(self,fav_sport):
		print(self.name + ' is playing '+ fav_sport)
g= Person('grayson','16','new york','male')
g.eat_fav_breakfast('cereal')
g.play_sport('basketball')
#lab_is_finished