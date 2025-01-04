print ("Learning Python")
print ("Week 1, Class 1: Functions and Variables")
print ("***************************************")
# print ("What is your name? ")
# input () # we need argument here
# input ("What is your name? ")


name = input("What is your name? ")
print("Hello,", name) # let, name is Sam
# output: Hello, Sam
print("Hello, ")
print(name)
"""
OUTPUT:
Hello,
Sam

but here I want:
Hello, Sam
"""
print("Hello, ", end="") # end will not move the cursor to next line
print(name)

"""
Expected Output
Hello, Sam
"""

print("Hello, ", end="????") # it also adds ???? b/w name and Hello
print(name)


print("Hello, ",name, sep="???") # separates Hello and NAME with ???


print("heello, {name}") # this prints as it is
# solve this we need f string - this is another way to solve this problem
print(f"Helllooo, {name}") # now this use name as a variable here

# str

name1 = input("Enter your name, with extra spaces before and after: ")
print("Name with extra spaces:", name1)

# to remove extra spaces
name1 = name1.strip() # it removes extra spaces
print("extra spaces removed:", name1)

# to capitalize first letter
name1 = name1.capitalize()
print("Name capitalized:", name1)
name1 = name1.title()
print("Title case: ", name1)


# we also can use functions to chain with each other

# removes extra spaces and change to title case of name1 string
name1= name1.strip().title()
print("removes spaces and makes title case:", name1)


# splitting a string
# split user's name into first and last name
first, last = name1.split(" ") # it splits name1 after space and assigns first to first variable and last part to last variable

print (f"Hello, {first}") # greet with last name

# greet with fullname
fullname = first+last
print (fullname)

