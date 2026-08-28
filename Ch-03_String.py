"""
String Operations in Python - Basics to Advanced
Author: Nikki Sharma
"""

def main():
    # Example strings
    name: str = "Nikki"
    word: str = "amazing"

    # 1. String Declaration
    a = 'Nikki'
    b = "Nikki"
    c = '''Nikki Sharma'''
    
    print(f"Strings: {a}, {b}, {c}")

    # 2. String Slicing
    # Index: N(0) i(1) k(2) k(3) i(4)
    print(f"\nOriginal String: {name}")
    print(f"Length: {len(name)}")
    print(f"Slicing [0:3]: {name[0:3]}")
    print(f"Negative Index [-1]: {name[-1]}")

    # 3. Slicing with skip value
    print(f"Slicing with skip [1:6:2] on 'amazing': {word[1:6:2]}")
    print(f"Reverse String [::-1]: {word[::-1]}")

    # 4. String Functions
    text = "Nikki"
    print(f"\nString Functions on '{text}':")
    print(f"endswith('kki'): {text.endswith('kki')}")
    print(f"count('k'): {text.count('k')}")
    print(f"capitalize(): {'nikki'.capitalize()}")
    print(f"find('kk'): {text.find('kk')}")
    print(f"replace('k', 't'): {text.replace('k', 't')}")

if __name__ == "__main__":
    main()
