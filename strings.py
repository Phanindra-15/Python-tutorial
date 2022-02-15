#slicing strings

b = "Hello, World!"
print(b[1:5])

b = "Hello, World!"
print(b[:6])

b = "Hello, World!"
print(b[-6:-2])

#modify strings

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())


#remove white spaces

a = "   Hello, World! "
print(a.strip())

#replace string
a = "Hello, World!"
print(a.replace("H", "W"))


#concatenate strings
a = "Hello"
b = "World"
c = a + b
print(c)

#boolean
a = 1
b = 3

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


x = "Hello"
y = 15

print(bool(x))
print(bool(y))
