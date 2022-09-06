
#scope
# a variable is available iside the region from it is created


def myfunc():
  x = 20
  print(x)

myfunc()



#function with in the functio

# a variable that can be accessed from a function within the function


def myfunc():
  x = 320
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

