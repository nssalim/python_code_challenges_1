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

# 4. MOVIE REVIEW
# Function that will help rate movies. The function will split the ratings into different ranges and tell the user how the movie was based on the movie’s rating.

# Define function to accept a single number called rating
# If the rating is equal to or less than 5, return "Avoid!"
# If the rating was less than 9, return "Excellent!"
# If neither of the if statement conditions were met, return "Don't Miss!"

def movie_review(rating):
  if(rating <= 5):
    return "Avoid!"
  if(rating < 9):
    return "Excellent!"
  return "Don't miss!!"
# test movie_review function:
print(movie_review(10))
# should print "Don't miss!"
print(movie_review(3))
# should print "Avoid!"
print(movie_review(7))
# should print "Excellent!"

# 5. MAX NUMBER
# Select which number from three input values is the greatest using conditional statements. Check the different combinations of values to see which number is greater than the other two. 

# Define a function that has three input parameters, num1, num2, and num3
# Test if num1 is greater than the other two numbers
# If so, return num1
# Test if num2 is greater than the other two numbers
# If so, return num2
# Test if num3 is greater than the other two numbers
# If so, return num3
# If there was a tie between the two largest numbers, then return "It's a tie!"

def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
# test max_num function:
print(max_num(-10, 0, 20))
# should print 20
print(max_num(-10, 1, -20))
# should print 1
print(max_num(-1, -10, -10))
# should print -1
print(max_num(1, 10, 10))
# should print "It's a tie!"
