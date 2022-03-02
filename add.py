def add(x):  
    return x+1  
def sub(x):  
    return x-1  
def operator(func, x):  
    temp = func(x)  
    return temp  
print(operator(sub,10))  
print(operator(add,20))  


#decorators in the concept if classess and objects


class Student:  
    def __init__(self,name,grade):  
         self.name = name  
         self.grade = grade  
    @property  
    def display(self):  
         return self.name + " got grade " + self.grade  
  
stu = Student("william","A")  
print("Name:", stu.name)  
print("Grade:", stu.grade)  
print(stu.display)
