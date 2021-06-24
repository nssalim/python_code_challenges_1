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

# 2. SAME NAME
# To check different names and determine if they are equal. Accept two strings and compare them.

# Define the function to accept two strings, your_name and my_name
# Test if the two strings are equal
# Return True if they are equal, otherwise return False

def same_name(your_name, my_name):
  if (your_name == my_name):
    return True
  else:
    return False
# test same_name function:
print(same_name("Sapphire", "Sapphire"))
# should print True
print(same_name("Sapphire", "Steel"))
# should print False

# 3. ALWAYS FALSE (Avoid creating conditions like this)
# An if statement that is always false is called a contradiction. A contradiction occurs when the condition will always be false no matter what value is passed into it.

# Define the function to accept a single parameter called num
# Use a combination of <, > and and to create a contradiction in an if statement.
# If the condition is true, return True, otherwise return False. 

def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False
# test  always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
