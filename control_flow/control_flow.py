# Python Code Challenges: Control Flow

# 1. LARGE POWER
# Method  tests whether the result of taking the power of one number to another number provides an answer which is greater than 3000. Use a conditional statement to return True if the result is greater than 3000 or return False if it is not. 

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


# 2. OVER BUDGET
# To watch budget in order to save money. Ensure the result of  spending is less than the total amount allocated for each of the categories. The function will accept a parameter called budget which describes spending limit. The next four parameters describe what the money is spent on. Sum all of the spendings and compare it to the budget. If over budget, return True. Otherwise return False. 

# Define the function to accept five parameters starting with budget then food_bill, electricity_bill, internet_bill, and rent
# Calculate the sum of the last four parameters
# Use if and else statements to test if the budget is less than the sum of the calculated sum from the previous step.
# If the condition is true, return True otherwise return False

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
# test over_budget function:
print(over_budget(100, 20, 30, 10, 30))
# should print False
print(over_budget(200, 50, 80, 40, 50))
# should print True

# 3. TWICE AS LARGE
# To determine if one number is twice as large as another number. Compare the first number with two times the second number. 

# Define function with two inputs num1 and num2
# Multiply the second input by 2
# Use an if statement to compare the result of the last calculation with the first input
# If num1 is greater then return True otherwise return False

def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False
# test twice_as_large function:
print(twice_as_large(4, 2))
# should print False
print(twice_as_large(5, 2))
# should print True


