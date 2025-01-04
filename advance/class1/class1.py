"""
What we going to clear in this class
Class: 1
Date: 01032025
1. strings
2. functions
and some programming techniques
"""

# asking for name, removing extra spaces before and after the O/P and also making it title case
name = input ("What is your name? ").strip().title()

# to greet with full name
print (f"Hello, {name}") # here f string use to print

# to greet with first name
# we need to split name first
first_name, last_name = name.split(" ") # it splits the name after space and stores first portion in first_name and last portion in last_name

print (f"Heellloo, {first_name}!")

# user defined functions
