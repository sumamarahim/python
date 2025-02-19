# x = int(input("What's x?"))
#
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# use to call the is_even and all other functions that are defined after the call
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# # method 1
# def is_even(n):
#     if n % 2 == 0:
#         return True # returns true for even
#     else:
#         return False # returns false for odd

# # method 2: better code of the above
# def is_even(n):
#     return True if n % 2 == 0 else False


# method 3: better code of the above
def is_even(n):
    return (n % 2 == 0)





main() # use to call the is_even and all other functions that are defined after the call
