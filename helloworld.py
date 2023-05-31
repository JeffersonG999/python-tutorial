a# Get started
print("Hello, World !")

# Indentation
if 5 > 2:
  print("Five is greater than two!")

if 5 > 2:
  print("Five is greater than two!") # two space
if 5 > 2:
    print("Five is greater than two!") # four space

# Variables
x = 5
y = "Hello, World!"
print(x)
print(y)

# Comment
print("Hello, World!")

# Cast
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x)
print(y)
print(z)

# Type
x = 5
y = "John"
print(type(x))
print(type(y))

# Single quote
x = "John"
print(x)

# Double quote
x = 'John'
print(x)

# Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Camel Case
myVariableName = "Jeff"
print(myVariableName)

# Pascal Case
MyVariableName = "Jeff"
print(MyVariableName)

# Snake Case
my_variable_name = "Jeff"
print(my_variable_name)

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

# Global Variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

y = "awesome"
def myfunc():
  y = "fantastic"
  print("Python is " + y)
myfunc()
print("Python is " + y)

def myfunc():
  global z
  z = "fantastic"
myfunc()
print("Python is " + z)

a = "awesome"
def myfunc():
  global a
  a = "fantastic"
myfunc()
print("Python is " + a)

# Data Type
x = "Hello World"
print(type(x))
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = range(6)
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
print(type(x))

# Setting the Specific Data Type
x = str("Hello World")
print(type(x))
x = int(20)
print(type(x))
x = float(20.5)
print(type(x))
x = complex(1j)
print(type(x))
x = list(("apple", "banana", "cherry"))
print(type(x))
x = tuple(("apple", "banana", "cherry"))
print(type(x))
x = range(6)
print(type(x))
x = dict(name="John", age=36)
print(type(x))
x = set(("apple", "banana", "cherry"))
print(type(x))
x = frozenset(("apple", "banana", "cherry"))
print(type(x))
x = bool(5)
print(type(x))
x = bytes(5)
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))

# Python Numbers
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

# Int
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

# Complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1 # int
y = 2.8 # float
z = 1j # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
import random

print(random.randrange(1, 10))

# Specify a Variable Type
# Integers
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)

# Floats
x = float(1) # x will be 1.0
y = float(2.8) # y will be 2.8
z = float("3") # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)

# Strings
x = str("s1") # x will be 's1'
y = str(2) # y will be '2'
z = str(3.0) # z will be '3.0'
print(x)
print(y)
print(z)

# Strings
print("Hello")

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Slicing
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
