# ==========================================
# PYTHON BASICS: FILE INPUT/OUTPUT (FILE I/O)
# ==========================================

import os

# Define a sample file name for testing
file_name = "sample.txt"

# 1. WRITING TO A FILE ('w' mode)
# Opens a file for writing. If the file doesn't exist, it creates one. 
# Note: 'w' mode overwrites existing content if the file already exists.
print("--- Writing to File ---")
with open(file_name, "w") as file:
    file.write("Hello, Python Developers!\n")
    file.write("This is a File I/O tutorial for beginners.\n")
print(f"Data successfully written to '{file_name}'.\n")


# 2. READING FROM A FILE ('r' mode)
# Opens a file for reading. The 'read()' method reads the entire content.
print("--- Reading from File ---")
with open(file_name, "r") as file:
    content = file.read()
    print("File Content:")
    print(content)


# 3. APPENDING TO A FILE ('a' mode)
# Opens a file for appending. It adds new data at the end without erasing old data.
print("--- Appending to File ---")
with open(file_name, "a") as file:
    file.write("Adding a new line at the end of the file.\n")
print("Data successfully appended.\n")


# 4. READING LINE BY LINE
# Useful for processing large files efficiently without loading everything at once.
print("--- Reading Line by Line ---")
with open(file_name, "r") as file:
    # readlines() returns a list of all lines in the file
    lines = file.readlines()
    for index, line in enumerate(lines, 1):
        print(f"Line {index}: {line.strip()}")


print("-" * 40)


# 5. CLEANUP (Optional)
# Removing the test file after execution so your directory stays clean.
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"Cleanup: '{file_name}' deleted successfully.")
  
