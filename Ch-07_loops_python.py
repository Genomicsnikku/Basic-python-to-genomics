# ==========================================
# PYTHON BASICS: LOOPS (FOR & WHILE)
# ==========================================

# 1. FOR LOOP
# Used for iterating over a sequence (like a list, tuple, string, or range).

print("--- FOR LOOP WITH RANGE ---")
# Print numbers from 0 to 4 using range()
for i in range(5):
    print(f"Current number: {i}")


print("\n--- FOR LOOP WITH LIST ---")
# Iterating through elements of a list
languages = ["Python", "JavaScript", "C++", "Java"]
for lang in languages:
    print(f"I love coding in {lang}")


print("-" * 40)


# 2. WHILE LOOP
# Executes a block of code repeatedly as long as the given condition is True.

print("--- WHILE LOOP ---")
count = 1
while count <= 3:
    print(f"While loop iteration count: {count}")
    count += 1  # Incrementing counter to avoid infinite loops


print("-" * 40)


# 3. LOOP CONTROL STATEMENTS (BREAK & CONTINUE)
# - 'break': Completely exits the loop.
# - 'continue': Skips the current iteration and moves to the next one.

print("--- USING BREAK STATEMENT ---")
for num in range(1, 6):
    if num == 4:
        print("Reached 4. Breaking the loop!")
        break
    print(f"Number: {num}")


print("\n--- USING CONTINUE STATEMENT ---")
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3...")
        continue
    print(f"Number: {num}")
      
