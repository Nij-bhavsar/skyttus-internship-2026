# No.1
print("Nij Bhavsar", "Age:21", "City:Pratapnagar")

# No.2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print(sum)

# No.3
temperature_celsius = float(input("Enter temperature in Celsius: "))
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print("Temperature in Fahrenheit:", temperature_fahrenheit)

# No. 4

name = input("Enter your name: ")
uppercase_name = name.upper()
print("Name in uppercase:", uppercase_name)

# No. 5

birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print("Your age is:", age)

# No. 6

val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))

swapped_val1 = val2
swapped_val2 = val1
print("After swapping: ")
print("First value:", swapped_val1)
print("Second value:", swapped_val2)

# No. 7

lenght = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = lenght * breadth
print("Area of rectangle:", area)

# No. 8

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")

# No. 9

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

avg = (num1 + num2) / 2
print("Average of the two numbers:", avg)
