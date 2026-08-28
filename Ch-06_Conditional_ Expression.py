# ==========================================
# PYTHON BASICS: CONDITIONAL STATEMENTS
# ==========================================

# 1. IF-ELIF-ELSE STATEMENTS
# Used to execute different blocks of code based on specific conditions.

age = 20
print(f"Checking age: {age}")

if age < 18:
    print("You are a minor.")
elif 18 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


print("-" * 40)


# 2. NESTED IF STATEMENTS
# An 'if' statement placed inside another 'if' or 'else' statement.

num = 15
print(f"Checking number: {num}")

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("The number is negative or zero.")


print("-" * 40)


# 3. TERNARY CONDITIONAL OPERATOR (SHORT-HAND IF-ELSE)
# A clean, single-line way to write simple conditional assignments.
# Syntax: value_if_true if condition else value_if_false

score = 75
print(f"Score: {score}")

result = "Pass" if score >= 50 else "Fail"
print(f"Result: {result}")
          
