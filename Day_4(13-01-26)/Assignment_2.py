#Python: Conditional Statements

## 1)Check if a person is eligible to vote (age ≥ 18).

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("This person is eligible to vote.")
# else:
#     print("This person is not eligible to vote.")

## 2)Grade calculator based on marks: 90+ = A, 80+ = B, else C.

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# else:
#     print("Grade: C")

## 3) Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

# light = input("Enter the traffic light color (Red/Yellow/Green): ").lower()
# if light == "red":
#     print("Stop!!!")
# elif light == "yellow":
#     print("Wait!")
# elif light == "green":
#     print("Go->>")

## 4)ATM withdrawal check: sufficient balance or not.

# balance = 25000
# withdrawal_amount = int(input("Enter the amount to withdraw: "))
# if withdrawal_amount <= balance:
#     print("There is sufficient balance.")
# else:
#     print("There is insufficient balance.")

## 5)Check if a number is positive, negative, or zero.

# num = int(input("Enter a number: "))
# if num > 0:
#     print(num, "is a positive number.")
# elif num < 0:
#     print(num, "is a negative number.")
# else:
#     print(num, "is zero.")

## 6)Check if a number lies within a given range.

# num = int(input("Enter a number: "))
# initial_num = int(input("Enter the lower bound of the range: "))
# end_num = int(input("Enter the upper bound of the range: "))
# if initial_num <= num <= end_num:
#     print(num, "lies within the range", initial_num, "to", end_num)
# else:
#     print(num, "does not lie within the range", initial_num, "to", end_num)

## 7)Username & password verification.

# username = "nijbhavsar"
# password = "thenb@23"
# input_username = input("Enter your username: ")
# input_password = input("Enter your password: ")

# if input_username == username and input_password == password:
#     print("Login successful!")  
# else:
#     print("Invalid username or password.")

## 8)Electricity bill calculator based on units consumed.

# units = int(input("Enter the number of electricity units consumed: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (units*5) + (units - 100) * 11
# else:
#     bill = (units*5) + (units - 100) * 11 + (units - 200) * 17
# print("The electricity bill is:", bill, "rupees.")

## 9) Simple calculator (add, subtract, multiply, divide).

# a = float(input("Enter value of a: "))
# b = float(input("Enter value of b: "))

# operation = input("Enter operation (+, -, *, /): ")
# if operation == "+":
#     print("The sum is:", a + b)
# elif operation == "-":
#     print("The difference is:", a - b)
# elif operation == "*":
#     print("The product is:", a * b)
# elif operation == "/":
#     if b != 0:
#         print("The quotient is:", a / b)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operation.")

## 10) Check type of triangle (equilateral, isosceles, scalene).

# side1 = float(input("Enter length of side 1: "))
# side2 = float(input("Enter length of side 2: ")) 
# side3 = float(input("Enter length of side 3: "))
# if side1 == side2 == side3:
#     print("The triangle is equilateral.")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is isosceles.")
# else:
#     print("The triangle is scalene.")