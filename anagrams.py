s1 = input("Enter first phrase : ")  
s2 = input("Enter second phrase : ")  
 
if set(s1.replace(' ','').lower()) == set(s2.replace(' ','').lower()):    #ignore case and spaces
      print("Strings are anagrams ")
else:
      print("Strings are not anagrams ")



print('-----------------')


y  = int(input('Enter a year : '))  
if  y%4==0  and y % 100 != 0  or  y%400==0:  
    print('Leap year')  
else:  
   print('Not a leap year')
