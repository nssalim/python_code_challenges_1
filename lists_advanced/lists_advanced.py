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

# *** To re-visit remove_middle function at later date ***


# 3. MORE FREQUENT ITEM
# Conveyor belt has items where each item is represented by a different number. Out of two items, find which one shows up more on belt. Use a function with three parameters. One parameter for the list of items, another for the first item being compared, and another for the second item.

# Define the function to accept three parameters: the list, the first item, and the second item
# Count the number of times item1 shows up in the list
# Count the number of times item2 shows up in the list
# If item1 shows up more, return item1. Otherwise, return item2
# If the two items appear the same number of times, return item1.

def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2
# check more_frequent_item function
print(more_frequent_item([7, 6, 6, 7, 6, 7, 6, 7, 6], 7, 6))
# should print 6

