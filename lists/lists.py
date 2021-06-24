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


# 3. LARGER LIST
# To work with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt.

# Define the function to accept two parameters for the two lists of numbers
# Check if the length of the first list is greater than or equal to the length of the second list
# If true, then return the last element from the first list. Otherwise, return the last element from the second list.

def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]
# test larger_list function
print(larger_list([9, 7, 6, 21], [-10, 27, 48, 75]))
# should print 21
# The larger_list function returns the last element of the list that contains more elements. As both lists are the same size, it returns the last element of my_list1.
