print ("Simple Calculator in Python\n\t***********")

# taking input
x = int(input("enter x: "))
y = int(input("enter y: "))

# calculating
sub = x - y
div = round(float(x/y), 2)
mul = x*y
rem = x%y

# prints the results
print (f"The sum of {x} and {y} is {x + y}")
print ("subtraction", sub)
print ("division", div)
print ("multiplication", mul)
print ("reminder", rem)
