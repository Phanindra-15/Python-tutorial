
#iterators in python

mytuple = ("phani", "sumanth", "yuvan")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


print('-----------------------------')

#Even strings are iterable objects in python

mystr = "sumanth"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


print('-----------------------')


#we canuse for loop to iterate through an iterable object

mytuple = ("phani", "sumanth", "yuvan")

for x in mytuple:
  print(x)

print('--------------------------------')


# wwe can iterate the character of string using for loop in python

mystr="phani"

for x in mystr:
    print(x)

