def show(text):
	return text.upper()

def wher(text):
	return text.lower()

def greet(func):
	
	greeting = func("Hi, I created  a function  and passed as an argument.")
	print (greeting)

greet(show)
greet(wher)

#another example4


def shiv(text):
	return text.lower()

def kev(text):
	return text.upper()

def greet(func):
	
	greeting = func("My Name is Punati Venkata Phanindra Kumar from Ongole.")
	print (greeting)

greet(shiv)
greet(kev)

