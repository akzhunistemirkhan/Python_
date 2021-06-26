mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))          #apple
                            #banana
                            #cherry
                            
mystr = "banana"
myit = iter(mystr)
print(next(myit))        #b
print(next(myit))        #a
print(next(myit))        #n
print(next(myit))        #a
print(next(myit))        #n
print(next(myit))        #a

#3
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))     #1
print(next(myiter))     #2
print(next(myiter))     #3
print(next(myiter))     #4
print(next(myiter))     #5

#4
class MyNumbers:
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
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:          # 1 ... 20
  print(x)

def myfunc():
  x = 300
  print(x)      #300
myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)        #300
  myinnerfunc()
myfunc()

x = 300
def myfunc():
  print(x)     #300
myfunc()
print(x)       #300

def myfunc():
  global x
  x = 300
myfunc()
print(x)

import mymodule
mymodule.greeting("Jonathan")  #Hello, Jonathan

import datetime
x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)
print(x)

import math
x = math.sqrt(64)
print(x)

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)     #{"name": "John", "age": 30, "city": "New York"}


import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))










