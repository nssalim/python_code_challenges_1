# Python Code Challenges: Control Flow (Advanced)

# 1. IN RANGE
# To test if a number falls within a certain range. Accept three parameters where the first parameter is the number being tested, the second parameter is the lower bound and the third parameter is the upper bound of the range.

# Define the function to accept three numbers as parameters
# Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound
# If this is true, return True, otherwise, return False

def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False
# test in_range function:
print(in_range(10, 9, 11))
# should print True
print(in_range(9, 10, 11))
# should print False
