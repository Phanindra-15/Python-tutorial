mytuple = ("phanindra", "sumanth", "yuvan")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#in case of strings

mystr = "jeevan"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#loop through an iterator

mytuple = ("phanindra", "sumanth", "yuvan")

for x in mytuple:
  print(x)

#iterate character of a string

mystr = "yuvan"

for x in mystr:
  print(x)


