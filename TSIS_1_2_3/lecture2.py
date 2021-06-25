thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])   # => cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # => ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])  # => ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])   # => ['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])   # => ['orange', 'kiwi', 'melon']

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)    # => ['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)   # => ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)    # => ['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # => ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)    # => ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # => ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)   # => ['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)   # => ['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)   # =>  ['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)   # => []

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)     # => apple
                  # banana
                  # cherry

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])      # => apple
                          # banana
                          # cherry
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]     # => apple
                                 # banana
                                 # cherry
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)           # ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)            # ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)            #['banana', 'cherry', 'kiwi', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)           #['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in range(10)]
print(newlist)          #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = [x for x in range(10) if x < 5]
print(newlist)       #[0, 1, 2, 3, 4]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)      # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)     # ['hello', 'hello', 'hello', 'hello', 'hello']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)     # ['apple', 'orange', 'cherry', 'kiwi', 'mango']

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)     # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)     # [23, 50, 65, 82, 100]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)     # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)      # [100, 82, 65, 50, 23]

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)  #Отсортируйте список в зависимости от того, насколько близко это число к 50:
print(thislist)     # [50, 65, 23, 82, 100]   

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)    # ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)     # ['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)    #  ['cherry', 'Kiwi', 'Orange', 'banana']

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)      # ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)      # ['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)              #['a', 'b', 'c', 1, 2, 3]

#EX
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
fruits[0] = "kiwi"
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#SETS
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)    # => True

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)      # => {'orange', 'cherry', 'banana', 'apple'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)      # => {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)      # => {"apple", "cherry"}

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")     #If the item to remove does not exist, discard() will NOT raise an error
print(thisset)     # => {"apple", "cherry"}

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(x) #removed item                     # cherry
print(thisset) #the set after removal      # {'banana', 'apple'}

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)                      #set()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)                # {'b', 'a', 1, 2, 'c', 3}

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}        #both union() and update() will exclude any duplicate items
set1.update(set2)
print(set1)                # {'c', 3, 'a', 'b', 2, 1}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)         # {'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)           # {'google', 'banana', 'microsoft', 'cherry'}

# EX
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#dict 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])  # Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)   # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print(len(thisdict))   # 3

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)  #dict_keys(['brand', 'model', 'year'])
thisdict["color"] = "white"
print(x)    # dict_keys(['brand', 'model', 'year', 'color'])
x = thisdict.values()
print(x)    # dict_values(['Ford', 'Mustang', 1964])
thisdict["year"] = 2020
print(x) # dict_values(['Ford', 'Mustang', 2020])
x = thisdict.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)   # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
#or 
thisdict.update({"color": "red"})
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)   #{'brand': 'Ford', 'year': 1964}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)    # {'brand': 'Ford', 'model': 'Mustang'}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# Arrays
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)   # ['Ford', 'Volvo', 'BMW', 'Honda']
cars.pop(1)
print(cars)   # ['Ford', 'BMW']
cars.remove("Volvo")
print(cars)    # ['Ford', 'BMW']

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)    # 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)         # John
print(p1.age)          # 36

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()     # Hello my name is John

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()       # Hello my name is John

p1 = Person("John", 36)
p1.age = 40
print(p1.age)     # 40

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()      # John Doe
#2
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()       # Mike Olsen

#3 
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)    # 2019


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()   # Welcome Mike Olsen to the class of 2019

































#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is ordered* and changeable. No duplicate members.



