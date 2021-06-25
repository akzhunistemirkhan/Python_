print("hello world")

if 5 > 2:
  print("Five is greater than two!")

myfirst_name = "John"

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = 3+5j
y = 5j
z = -5j
print(type(x))    # <class 'complex'>
print(type(y))
print(type(z))

import random
print(random.randrange(1, 10))   # 6

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

a = "Hello, World!"
print(a[1])   # e

for x in "banana":
  print(x)       #b
                 #a
                 #n
                 #a
                 #n
                 #a

txt = "The best things in life are free!"
print("free" in txt)   # True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))   # My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  # I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # I want to pay 49.95 dollars for 3 pieces of item 567

#This is a comment

"""
This is a comment
written in 
more that just one line
"""

# Which one is NOT a legal variable name?  => MY-VAR
# In Python, 'Hello', is the same as "Hello"
# Which method can be used to remove any whitespace from both the beginning and the end of a string? => strip()
# Which method can be used to replace parts of a string? => replace()
# Which of these collections defines a LIST? ["apple", "banana", "cherry"]
# TUPLE => ("apple", "banana", "cherry")
# SET => {"apple", "banana", "cherry"}
# Which collection is ordered, changeable, and allows duplicate members? => LIST
# Which collection does not allow duplicate members? SET
# Which statement is used to stop a loop? Break

 #What is the correct way to create a function in Python? => def myfunction():

def myfunc():
  global x
  x = "fantastic"

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = 5
print(type(x))
#int

x = "Hello World"
print(type(x))
#str

x = 20.5
print(type(x))
#float

x = ["apple", "banana", "cherry"]
print(type(x))
#list

x = ("apple", "banana", "cherry")
print(type(x))
#tuple

x = {"name" : "John", "age" : 36}
print(type(x))
#dict

x = True
print(type(x))
#bool

#STRINGS
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]        # => llo

txt = "Hello World"
txt = txt.upper()
txt = txt.lower()

#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])           #Hello

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list = []
for x in fruits:
  if "a" in x:
    list.append(x)
print(list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list = [x for x in fruits if "a" in x]
print(list)

list = ["apple", "banana", "cherry"]
print(list[-1])

# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string















