# Python Code Challenges: Lists

# 1. APPEND SIZE
# To calculate the length of a list and then append a value to the end of the list.

# Define the function to accept one parameter for the list
# Get the length of the list
# Append the length of the list to the end of the list
# Return the modified list

def append_size(my_list):
  my_list.append(len(my_list))
  return my_list
# test append_size function:
print(append_size([9, 7, 6, 21]))
# The function appends the size of my_list (inclusive) to the end of my_list. The function then returns this new list.

# As my_list was [9, 7, 6, 21], the function returns [9, 7, 6, 21, 4] because the size of my_list was originally 4.


# 2. APPEND SUM
# To calculate the sum of the last two elements of a list and append it to the end. Function will repeat process two more times and return the resulting list.

# Define the function to accept one parameter for the list of numbers
# Add the last and second to last elements from the list together
# Append the calculated value to the end of the list.
# Repeat steps 2 and 3 two more times
# Return the modified list

def append_sum(my_list):
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  my_list.append(my_list[-1] + my_list[-2])
  return my_list
print(append_sum([9, 7, 6, 21]))
# The function adds the last two elements of my_list together and appends the result to my_list. It does this process three times and then return my_list.

# As my_list started as [9, 7, 6, 21], the final result should be [9, 7, 6, 21, 27, 48, 75].

