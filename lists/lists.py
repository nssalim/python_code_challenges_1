# Python Code Challenges: Lists

# 1. APPEND SIZE
# To calculate the length of a list and then append a value to the end of the list.

# Define the function to accept one parameter for the list
# Get the length of the list
# Append the length of the list to the end of the list
# Return the modified list

def append_size(lst):
  lst.append(len(lst))
  return lst
# test append_size function:
print(append_size([9, 7, 6, 21,]))
# should print [9, 7, 6, 21, 4] because the size of lst was originally 4