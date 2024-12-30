# this code is written on linux terminal

# shifting my knowledge of CPP programming in python


# variables etc

# function with name user_age()
def user_age():
	print ("What is your age?")
age = user_age() # function called and stored in a variable
print (age)
myint = 17 # int type 
myfloat = 3.7 # flaot type data
myname = "Sumama Rahim - double quote"
myname2 = 'Sumama Rahim - single quote'
mygender = 'M'
print (float(myint)) # converts int into float num
print (myint)
print (myname)
print (myname2)
print (mygender)
print ("Hello world! my name ", myname)
print (type(myint)) # prints type of myint variable
print (type(myname)) # prints type of myname variable
# assigning multiple variables
x, y, z = "Orange", "Blue", "Red"
print (x , y , z) # prints above 3 variables
print (x, z)

# one value to multiple variables
a = b = c = "Green"
print (a)
print (b)
print (c)

# unpacking - in later chaps we'll learn in details
fruits = "Apple", "Banana", "Mange"
print (fruits) # it prints all the values in above variables
i = j = k = fruits
print (i)
fruits2 = ["Mango", "Banana", "Apple", "Peach"]
a = b = c = d = fruits2
print (a)

x = 4
y = 5
print (x+y)
x = 3
y = "Pakistan"
#print (x+y) # throughs error, int and str can't be add with each other
print (x,y) 

# global variables
x = "This is global variable"
def my_func():
	y2 = "This is local variable" # local variable and the scope will be limited to this function only
	print (x)
	print (y2)
my_func()

p = "Fantastic" # global declared
def new_function():
	p = "Awesome" # local decalared
	print ("Python is " + p) # use here local variable, cz it overwrite the global
new_function()
print ("Python is " + p) # use here global variable
# dry run
# new_function called nd it prints "Python is Awesome"
# new line prints "Python is Fantastic"

# so we can change any local variable to global variable by using "GLOBAL" keyword
def function_used_global_variable():
	variable = 19 # local scope
	print (variable)
	global variable2 # global scope
	variable2 = 21
	print (variable2)

function_used_global_variable()
print ("Printing the global var from function_used_global_variable() function", variable2)
print ("hello", "world!")



print ("*** Data Types in Python ***")
# data types in python
# built in types 

# NOTE: to confirm the type of following, use type() function to verify


# text type: str
name = "Sumama"
print (name)
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# multi line string
a = """Lorem ipsum dolor sit amet
consectetur adipiscing elit
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print (a)


# String as array

name = "Sumama"
print ("string as array: ", name[3])

# looping through string

x = 0
print ("looping through string")
for x in name:
	print (x)

# finding length of string/array
print ("Length of string: ", len(name))

# checking certain thing in strings
message = "Programming is the most important job in everyone life"
print (message)
# finding "life" in above variable
print ("life" in message) # it returns True if found required  information
# checking if life is found or not in the string
if "life" in message:
	print ("'life' is found in above string")
else:
	print ("not found")

# check if not in
if "life" not in message:
	print ("'life' is not in the string")
else:
	print ("'life' is in the string")



# num: int, float, complex
age = 1
num = 28273983274837
print ("Num: ", num, "Type is: ", type(num))
num = -23323
print (num, "type is: ", type(num))
print (age)


height = 5.7
num = 23E7
print ("23E7: ", num, " and type is: ", type(num))
print (height)
complex_var = 7j
print ("Complex: ", complex_var)

# sequences type: list, tuple, range
list_var = ["Cherry", "Banana", "Apple"]
print ("List: ", list_var)
tuple_var = ("Apple", "Cherry", "Banana")
print ("Tuple: ", tuple_var)
range_var = range(6)
print ("Range: ", range_var)

# mapping type: dict
person = {"Name" : "Someon", "Age" : 19}
print ("Mapping: ", person)

# set types: set, frozenset
set_var = {"Apple", "Mango", "Berry"}
print ("Set: ", set_var)
frozenset_var = frozenset ({"Mange", "Berry", "Apple"})
print ("Frozenset: ", frozenset_var)

# Booolean: bool
option = True
print ("Do I am here?", option)

# binary types: bytes, bytearray, memoryview
bytes_var = b"Hello"
print ("Byte: ", bytes_var)

bytearray_var = bytearray(5)
print ("bytearray: ", bytearray_var)

memoryview_var = memoryview(bytes(5))
print ("Memoryview: ", memoryview_var)

# none type: NoneType
x = None
print ("None type variable: ", x)

# we can know the type of data by using type() function

# type casting can be done on all the above variables





# print (y2) # calling y which is not declared in this scope
# Data types and variables
# control structures - loops, if else if
# functions



