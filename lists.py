#creating list

thislist = ["apple", "banana", "cherry"]
print(thislist)

#allowance of duplicates

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#number of lists

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#accessing items in list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#negative indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#change list items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "guava"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["guava"]
print(thislist)

#add items in the list

thislist = ["apple", "banana", "cherry"]
thislist.append("guava")
print(thislist)

#insert items at specified location

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "guava")
print(thislist)

#appending one list with another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "guava", "jack fruit"]
thislist.extend(tropical)
print(thislist)

#loop

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#sort lists
thislist = ["orange", "mango", "kaja", "apple", "banana","guava","jack fruit"]
thislist.sort()
print(thislist)


thislist = [10, 5, 15, 2, 13]
thislist.sort()
print(thislist)
