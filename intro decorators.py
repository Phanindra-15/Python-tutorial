
#introduction to decorators

def func1(msg):  
    print(msg)  
func1("Hii")  
func2 = func1  
func2("Hii")


#inner function using decorators

def func():  
     print("We are in first function")  
     def func1():  
           print("This is first child function")  
     def func2():  
           print(" This is second child function")  
     func1()  
     func2()  
func()  
