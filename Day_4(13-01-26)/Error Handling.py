# 1)Write a program to handle division by zero error.

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
try:
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2)Write a program to handle invalid integer input.

input_str = input("Enter an integer: ")
try:
    value = int(input_str)
    print("You entered the integer:", value)
except ValueError:
    print("Error: Invalid input!!. Please enter a valid integer.")

# 3)Write a program to open a file and handle the “file not found” error.

file_name = input("Enter the file name to open: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found!!. Please check the file name and try again.")

# 4)Write a program to demonstrate multiple exception blocks.

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input!!. Please enter valid integers.")

# 5)Write a program to use finally for resource cleanup.

file = None
try:
    file_name = input("Enter the file name to open: ")
    file = open(file_name, 'r')
    content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found!!. Please check the file name and try again.")
finally:
    file.close()
    print("File has been closed.")

# 6) Write a program to create a custom exception for invalid age (<18).

class InvalidAgeError(Exception):
    pass
age = int(input("Enter your age: "))
try:
    if age < 18:
        raise InvalidAgeError("Age is less than 18.")
    print("Valid age.")
except InvalidAgeError as e:
    print("Error:", e)

# 7)Write a program to handle IndexError when accessing a list.

list_1 = [11, 22, 33, 44, 55]
index = int(input("Enter the index to access (0-4): "))
try:
    value = list_1[index]
    print("Value at index", index, "is:", value)
except IndexError:
    print("Error: Index out of range!!. Please enter a valid index between 0 and 4.")

# 8)Write a program that takes two numbers and handles all possible errors.

try:
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    result = n / m
    print("The result of division is:", result)
except ValueError:
    print("Error: Invalid input!!. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 9) Write a program to log errors to a file instead of printing them.

import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

try:
    n = int(input("Enter first value: "))
    m = int(input("Enter second value: "))
    result = n / m
    print("The result of division is:", result)
except ValueError:
    logging.error("Error: Invalid input!!. Please enter valid numbers.")
except ZeroDivisionError:
    logging.error("Error: Division by zero is not allowed.")
print("Errors have been logged to error1_log.txt.")

# 10)Write a program that validates an email format and raises an exception for invalid ones.

import re
class InvalidEmailError(Exception):
    pass
email = input("Enter your email address: ")
try:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format.")
    print("Valid email address.")
except InvalidEmailError as e:
    print("Error:", e)