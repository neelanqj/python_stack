class Animal(object):
	def __init__(self, name, health):
        	self.name = name
		self.health = health

    	def walk(self):
        	self.health = self.health - 1
        	return self

    	def run(self):
        	self.health = self.health - 5
        	return self

	def display_health(self):
		print str(self.health)
		return self

animal1 = Animal("animal", 100)
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
	def __init__(self):
		self.name = "Dog"
		self.health = 150

	def pet(self):
		self.health = self.health + 5
		return self

dog1 = Dog()
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
	def __init__(self):
		self.name = "Dragon"
		self.health = 170

	def fly(self):
		self.health += -10

	def display_health(self):
		super(Dragon, self)
		print "I am dragon"

		return self

animal_test = Animal("test",100)

animal_test.pet()
animal_test.fly()
animal_test.display_health()

dog_test = Dog()
dog_test.fly()