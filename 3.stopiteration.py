#we can stop the iteration over thecertin period of range
# for this we should the concept of raise stop iteration which helps to stop the iteration over the certain amount of range


class numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = numbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
