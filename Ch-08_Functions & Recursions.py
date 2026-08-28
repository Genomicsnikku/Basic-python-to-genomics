# ==========================================
# PYTHON BASICS: FUNCTIONS & RECURSION
# ==========================================

# 1. BASIC FUNCTION DEFINITION & CALLING
# A function is a block of reusable code that performs a specific task.

def greet_user(name):
    """Function to greet a user by name."""
    print(f"Hello, {name}! Welcome to Python programming.")

# Calling the function
greet_user("Rahul")
greet_user("Priya")


print("-" * 40)


# 2. FUNCTION WITH RETURN VALUE
# Functions can process data and return the result using the 'return' keyword.

def add_numbers(num1, num2):
    """Function to add two numbers and return the sum."""
    return num1 + num2

# Storing the returned value in a variable
result = add_numbers(15, 25)
print(f"Sum of the two numbers: {result}")


print("-" * 40)


# 3. DEFAULT PARAMETERS
# You can provide default values for parameters in case no argument is passed.

def display_profile(username, country="India"):
    """Function with a default parameter for country."""
    print(f"User: {username}, Country: {country}")

display_profile("Aman")             # Uses default country 'India'
display_profile("John", "USA")       # Overrides default country


print("-" * 40)


# 4. RECURSION (FUNCTION CALLING ITSELF)
# Recursion is a technique where a function calls itself to solve a smaller sub-problem.
# It requires a base condition to stop the recursive calls (preventing infinite loops).

def calculate_factorial(n):
    """Recursive function to find the factorial of a number."""
    # Base condition: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive call
        return n * calculate_factorial(n - 1)

# Testing the recursive function
number = 5
factorial_result = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial_result}")
