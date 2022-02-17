
#creating class and objects
class Dog:

	
	attr1 = "mammal"

	
	def __init__(self, name):
		self.name = name


maxi = Dog("maxi")
dax = Dog("dax")


print("maxi is a {}".format(maxi.__class__.attr1))
print("Tommy is also a {}".format(dax.__class__.attr1))


print("My name is {}".format(maxi.name))
print("My name is {}".format(dax.name))

#creating class and objects with methods

class Dog:

	
	attr1 = "mammal"

	
	def __init__(self, name):
		self.name = name
		
	def speak(self):
		print("My name is {}".format(self.name))


maxi = Dog("maxi")
daxi = Dog("daxi")


maxi.speak()
daxi.speak()
