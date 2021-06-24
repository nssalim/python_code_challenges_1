# Python Code Challenges: Control Flow

# 1. LARGE POWER
# method  tests whether the result of taking the power of one number to another number provides an answer which is greater than 3000. Use a conditional statement to return True if the result is greater than 3000 or return False if it is not. 

# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 3000. If it is then return True. Otherwise, return False

def large_power(base, exponent):
  if base ** exponent > 3000:
    return True
  else:
    return False
# test large_power function:
print(large_power(10, 4))
# should print True
print(large_power(10, 3))
# should print False

