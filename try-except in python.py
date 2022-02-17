#THE TRY BLOCK WILL GENERATE AN EXCEPTION BECAUSE X VALUE IS NOT DEFINED\

try:
  print(x)
except:
  print("An exception occurred")

print('----------------------')

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except :
  print("Something else went wrong")

#WE CAN USE ELSE KEYWORD TO DEFINE A BLOCK OF CODE TO BE EXCUTED IF NO ERRORS WERE RAISED

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#THE FINALLY BLOCK IS SPECIFIED IF THE TRY BLOCK RAISES AN ERROR

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#RAISE EXCEPTION

x = 1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
print(x)
