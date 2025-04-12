# """
# Python Function Practice Exercises
# This file contains various exercises to help you master functions in Python.
# Try to solve each exercise on your own!
# """

# # Exercise 1: Basic Function
# # Create a function that takes a name as input and returns a greeting message
# def greet(name):
#     return f"Hello, {name}! Welcome to Python functions!"

# # Exercise 2: Function with Multiple Parameters
# # Create a function that calculates the area of a rectangle
# def calculate_rectangle_area(length, width):
#     return length * width

# # Exercise 3: Function with Default Parameters
# # Create a function that creates a greeting with a default greeting message
# def create_greeting(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# # Exercise 4: Function that Returns Multiple Values
# # Create a function that calculates both area and perimeter of a rectangle
# def calculate_rectangle_metrics(length, width):
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter

# # Exercise 5: Function with Type Hints
# # Create a function that adds two numbers with type hints
# def add_numbers(a: float, b: float) -> float:
#     return a + b

# # Exercise 6: Function with *args
# # Create a function that calculates the average of any number of numbers
# def calculate_average(*numbers):
#     if not numbers:  # Handle empty input
#         return 0
#     return sum(numbers) / len(numbers)

# # Exercise 7: Function with **kwargs
# # Create a function that creates a person dictionary with any number of attributes
# def create_person(**attributes):
#     return attributes

# # Exercise 8: Recursive Function
# # Create a function that calculates factorial using recursion
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Exercise 9: Lambda Function
# # Create a lambda function that squares a number
# square = lambda x: x ** 2

# # Exercise 10: Function with Docstring
# # Create a function that calculates BMI with proper documentation
# def calculate_bmi(weight: float, height: float) -> float:
#     """
#     Calculate the Body Mass Index (BMI) for a given weight and height.
    
#     Args:
#         weight (float): Weight in kilograms
#         height (float): Height in meters
        
#     Returns:
#         float: BMI value
        
#     Example:
#         >>> calculate_bmi(70, 1.75)
#         22.86
#     """
#     return weight / (height ** 2)

# # Practice Problems:
# # Try to solve these problems on your own!

# # Problem 1: Create a function that checks if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):  # More efficient implementation
#         if number % i == 0:
#             return False
#     return True

# # Problem 2: Create a function that finds the largest number in a list
# def find_largest(numbers):
#     if not numbers:  # Handle empty list
#         return None
#     return max(numbers)  # Using built-in max function

# # Problem 3: Create a function that counts vowels in a string
# def count_vowels(text):
#     vowels = "aeiouAEIOU"  # Include both uppercase and lowercase
#     return sum(1 for char in text if char in vowels)

# # Problem 4: Create a function that reverses a string
# def reverse_string(text):
#     return text[::-1]

# # Problem 5: Create a function that checks if a string is a palindrome
# def is_palindrome(text):
#     return text == text[::-1]

# # Test your solutions here:
# if __name__ == "__main__":
#     # Test Exercise 1
#     print(greet("Alice"))  # Should print: Hello, Alice! Welcome to Python functions!
    
#     # Test Exercise 2
#     print(calculate_rectangle_area(5, 3))  # Should print: 15
    
#     # Test Exercise 3
#     print(create_greeting("Bob"))  # Should print: Hello, Bob!
#     print(create_greeting("Bob", "Hi"))  # Should print: Hi, Bob!
    
#     # Test Exercise 4
#     area, perimeter = calculate_rectangle_metrics(5, 3)
#     print(f"Area: {area}, Perimeter: {perimeter}")  # Should print: Area: 15, Perimeter: 16
    
#     # Test Exercise 5
#     print(add_numbers(3.5, 2.5))  # Should print: 6.0
    
#     # Test Exercise 6
#     print(calculate_average(1, 2, 3, 4, 5))  # Should print: 3.0
    
#     # Test Exercise 7
#     person = create_person(name="Charlie", age=25, city="New York")
#     print(person)  # Should print: {'name': 'Charlie', 'age': 25, 'city': 'New York'}
    
#     # Test Exercise 8
#     print(factorial(5))  # Should print: 120
    
#     # Test Exercise 9
#     print(square(4))  # Should print: 16
    
#     # Test Exercise 10
#     print(calculate_bmi(70, 1.75))  # Should print: 22.86
    
#     # Test Problem 1
#     print(is_prime(17))  # Should print: True
#     print(is_prime(20))  # Should print: False
    
#     # Test Problem 2
#     print(find_largest([1, 5, 3, 9, 2]))  # Should print: 9
    
#     # Test Problem 3
#     print(count_vowels("Hello World"))  # Should print: 3
    
#     # Test Problem 4
#     print(reverse_string("Python"))  # Should print: nohtyP
    
#     # Test Problem 5
#     print(is_palindrome("radar"))  # Should print: True
#     print(is_palindrome("python"))  # Should print: False



def function_new(a : int,b : int) -> int:
    result = a + b
    return result

print(function_new(10,20))

def full_name(first_name : str, last_name : str) -> str:
    return f"Your full name is {first_name.title() + " " + last_name.title()}"
print(full_name("sai","teja"))


