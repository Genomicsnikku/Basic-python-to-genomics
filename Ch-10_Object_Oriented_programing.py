# ==========================================
# PYTHON ADVANCED: OBJECT-ORIENTED PROGRAMMING (OOP)
# ==========================================

# 1. CLASS AND OBJECT DEFINITION
# A class is a blueprint for creating objects, and an object is an instance of a class.

class Employee:
    # Class attribute (shared by all instances)
    company_name = "Tech Solutions Inc."

    def __init__(self, name, salary, role):
        # Instance attributes (unique to each object)
        self.name = name
        self.salary = salary
        self.role = role

    def show_details(self):
        """Method to display employee details."""
        print(f"Employee: {self.name} | Role: {self.role} | Salary: ${self.salary} | Company: {Employee.company_name}")


print("--- Creating Objects ---")
emp1 = Employee("Alice", 75000, "Software Engineer")
emp2 = Employee("Bob", 90000, "Project Manager")

emp1.show_details()
emp2.show_details()


print("-" * 50)


# 2. INHERITANCE
# Inheritance allows a child class to inherit attributes and methods from a parent class.

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Child Class inheriting from Person
class Developer(Person):
    def __init__(self, name, age, programming_language):
        # Super() function is used to call the constructor of the parent class
        super().__init__(name, age)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")


print("--- Demonstrating Inheritance ---")
dev = Developer("Charlie", 26, "Python")
dev.introduce()       # Inherited method from Person class
dev.write_code()      # Unique method to Developer class


print("-" * 50)


# 3. ENCAPSULATION & ACCESS MODIFIERS
# Encapsulation hides private data using underscores (_ for protected, __ for private) 
# and provides getter/setter methods to access or modify it securely.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (hidden from outside)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount}.")
        else:
            print("Invalid deposit amount!")

    def get_balance(self):
        """Getter method to securely view private balance."""
        return self.__balance


print("--- Demonstrating Encapsulation ---")
account = BankAccount("David", 1000)
account.deposit(500)
print(f"Current Balance for {account.owner}: ${account.get_balance()}")
# Direct access like account.__balance will throw an AttributeError (Data Security!).


print("-" * 50)


# 4. POLYMORPHISM
# Polymorphism allows different classes to have methods with the same name 
# but different implementations.

class Dog:
    def make_sound(self):
        return "Bark! 🐶"

class Cat:
    def make_sound(self):
        return "Meow! 🐱"

def animal_voice(animal_object):
    """Function that accepts any object with a 'make_sound' method."""
    print(animal_object.make_sound())


print("--- Demonstrating Polymorphism ---")
dog = Dog()
cat = Cat()

animal_voice(dog)
animal_voice(cat)
          
