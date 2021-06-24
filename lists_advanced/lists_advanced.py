# Python Code Challenges: Lists (Advanced)

# 1. EVERY SEVEN NUMBERS
# Function creates a list of numbers up to 100 in increments of 7 starting from a number that is passed to the function as an input parameter.

# Define the function to accept one parameter for the starting number
# Calculate the numbers between the starting number and 100 while incrementing by 7
# Store the numbers in a list
# Return the list

def every_seven_nums(start):
  return list(range(start, 102, 7))
# test every_seven_nums function:
print(every_seven_nums(22))
# should print [22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]
# every_seven_nums function returns a list of every seventh number between start and 102 (inclusive). The function every_seven_nums(22)  returns the list [22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]. If start is greater than 102, the function returns an empty list.


# 2. REMOVE MIDDLE
# Function to remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an ending index. All elements with an index between the starting and ending index to be removed from the list.

# Define the function to accept three parameters: the list, the starting index, and the ending index
# Get all elements before the starting index
# Get all elements after the ending index
# Combine the two partial lists into the result
# Return the result

def remove_middle(my_list, start, end):
  return my_list[:start] + my_list[end+1:]
# test remove_middle function:
print(remove_middle([9, 7, 6, 21, 48, 75, 23], 1, 3))
# should print [9, 48, 75, 23]
print(remove_middle([9, 7, 6, 21, 48, 75, 23], 1, 2))
# should print [9, 21, 48, 75, 23]

