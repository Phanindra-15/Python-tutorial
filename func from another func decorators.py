
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15(10))

#another example




def create_aidd(x):
	def aedd(y):
		return x+y

	return aedd

add_15 = create_aidd(15)

print(add_15(100))

