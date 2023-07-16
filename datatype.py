# different opperations on strings
# data types
#case sensitive language
print("Hello World")
int(4.3)
print(float(5))
print(type(4.3))
print(bool(1))
print(int("2"))
print(int(True))
print(25/5) # its output will be in float by default in python 3
print(25/6)
print(25//5) # its output will be in int due to //
print(25//6)
print(2*60+30)
print(30+60*2)
my_var = 1
print(my_var)
my_var = 10
print(my_var)
x = 5 + 51 +3
y = x/20
print(y)
print(type(x))
print(type(y))

#convert minutes into hours
total_min = 397
total_hours = total_min/60
print("total minutes", total_min, " will be in total hours", total_hours)

# String Operations
name = 'Sumama Rahim'
print(name)
print(name[3])
print(name[7])
print(name[6])
print(name[::2]) #called stide value #prints even index
print(name[0:4]) #String Slicing
print(name[5:9])
print(name[0::]) # prints string of name var from 0 index means start to the End
print(name[::3])
print(name[0:5:2]) # it prints from 0 index to 5 index but gaps b/w them will be 2
print(name[0:9:2])
print(name[0:8:3])
print(name[2:8:3])

#tuples slicing
# len Command
print(len(name)) # it prints 12 because name var have 12 char in length and index 11 becaus it starts from 0 so 11+1 is 12
print("So the length of ", name, "is ", len(name))
print(len("Pakistan"))

#string Concatenation
concatenateString = name+ " is here"
print(name+" was a student of 12")
print(concatenateString)

#String Replicate

print(3*" sumama")
print(3* name)

#String Immutable
#means you can't change var's value but can create new var
name1 = "Sumama"
# name1[0] = "C" -- Gives error because we can't change the value of index 0
num1 = 101
name1 = "C"+"umama"
print(name1)

#String Escape Sequences
print("Pakistan is a second largest\t country of Muslims \nafter Indonesia") #\t for tab\n for new line \a for alart

# both prints \ -- two different methods
print("Pakistan\\Islamic Republic of Pakistan")
print(r"Pakistan\Islamic Republic of Pakistan")


# String Methods
a = "Smart Study"
b = a.upper() # upper is a method
print(b)

timeNow = "its 11 o'clock right now"
timeNow1 = timeNow.replace("11","9") #replace will replace 9 instead of 11
print(timeNow1)

counting = a
countinga = counting.count(counting)
print(countinga)

# string Stride
find1 = name.find("ma")
print(find1)
find2 = name.find("Ra")
print(find2)
find3 = name.find(" ")
print(find3)
#in sub string is not in string it prints -1
find4 = name.find("Khan")
print(find4) # prints -1

# assignment
find5 = "026924".find("6")
print(find5)

