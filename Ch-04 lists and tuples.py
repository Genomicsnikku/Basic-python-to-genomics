# ==========================================
# PYTHON BASICS: LISTS VS TUPLES
# ==========================================

# 1. PYTHON LISTS []
# Lists are mutable, meaning you can modify, add, or remove items after creation.

# Create a list
fruits = ["apple", "banana", "mango"]
print("Original List:", fruits)

# Access an element using index (Indexing starts from 0)
print("First fruit:", fruits[0])

# Modify an element (Lists are mutable)
fruits[1] = "grapes"
print("Modified List:", fruits)

# Add a new element to the end of the list
fruits.append("orange")
print("After append:", fruits)

# Remove a specific element from the list
fruits.remove("apple")
print("After remove:", fruits)


print("-" * 40)


# 2. PYTHON TUPLES ()
# Tuples are similar to lists, but they are immutable (read-only).
# Once created, you cannot change, add, or remove elements.

# Create a tuple
colors = ("red", "green", "blue")
print("Original Tuple:", colors)

# Access an element using index
print("First color:", colors[0])

# Note: Trying to modify a tuple will raise a TypeError:
# colors[1] = "yellow"  -> Uncommenting this will cause an error!

# Find the total number of elements in the tuple
print("Total colors:", len(colors))
