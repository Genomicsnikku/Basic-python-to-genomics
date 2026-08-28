# ==========================================
# PYTHON BASICS: DICTIONARIES & SETS
# ==========================================

# 1. PYTHON DICTIONARIES ({})
# Dictionaries store data in key-value pairs. They are mutable, 
# and keys must be unique.

# Create a dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Computer Science"
}
print("Original Dictionary:", student)

# Access a value using its key
print("Student Name:", student["name"])

# Modify an existing value
student["age"] = 22
print("Updated Age:", student["age"])

# Add a new key-value pair
student["city"] = "Delhi"
print("After Adding City:", student)

# Remove a key-value pair
del student["course"]
print("After Deletion:", student)


print("-" * 40)


# 2. PYTHON SETS ({})
# Sets are unordered collections of unique elements. 
# They automatically remove duplicate values and are mutable.

# Create a set (Notice duplicate 'apple' will be removed automatically)
fruits_set = {"apple", "banana", "mango", "apple"}
print("Original Set (Duplicates removed):", fruits_set)

# Add a new element to the set
fruits_set.add("orange")
print("After Adding Element:", fruits_set)

# Remove an element from the set
fruits_set.remove("banana")
print("After Removing Element:", fruits_set)

# Set operations (Union and Intersection)
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union of sets:", set_a.union(set_b))          # Combines both sets (no duplicates)
print("Intersection of sets:", set_a.intersection(set_b)) # Finds common elements
