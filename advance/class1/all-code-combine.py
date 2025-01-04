print ("Class 1's all code combined in one app")

"""
WAP to do following
marks sheet
takes from the user
1. enter name
2. enter marks of 3 subjects out of 100 each
returns to the user
1. greet with first name
2. each subject marks with %age
3. total taken marks
4. average marks
guidlines
use def
1. for calculations and taking marks
"""


# taking name from the user
full_name = input ("Enter your full name: ").strip().title()
first_name, last_name = full_name.split(" ")

# greeting to user
print (f"Heellloo, {first_name}")
# taking marks or 3 subjects out of 90 each
def taking_and_calc_marks():
	marks1 = int(input("enter marks 1: "))
	marks2 = int(input("enter marks 2: "))
	marks3 = int(input("enter marks 3: "))
	total = marks1 + marks2 + marks3
	avg = total/3
	percentage = (total*100)/270
	# calculating them
	print ("Your total marks is:", total, "out of 270")
	print ("Your average marks is:", round(avg, 2))
	print ("Your %age is:",round(percentage, 2))

# calling function
taking_and_calc_marks()
