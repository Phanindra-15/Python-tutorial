
#ISON IS USED TO STORE AND EXCHANGE THE DATA

#convert from json to python

import json
x =  '{ "name":"phanindra", "age":20, "city":"rajamandry"}'

y = json.loads(x)

print(y["age"])
print(y["name"])
print(y["city"])


#convert rom python to json

import json

x = {
  "name": "phanindra",
  "age": 20,
  "city": "ongole"
}


y = json.dumps(x)


print(y)

#we can convert python objects into json for

import json

print(json.dumps({"name": "phani", "age": 21}))
print(json.dumps(["atlas", "book"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello world"))
print(json.dumps(32))
print(json.dumps(3.7))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
