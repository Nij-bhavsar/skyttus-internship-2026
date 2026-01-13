# Python: Loops

# 1)Print numbers from 1 to 10.

for i in range(1, 11):
    print("The Numbers are:", i)

# 2)Display multiplication table for a given number.

num = int(input("Enter a number to display its multiplication table:"))
print("The number for multiplication table is", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 3)Find factorial of a number.

num = int(input("Enter a number to find its factorial:"))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("The factorial of", num, "is", fact)

# 4)Generate the first N Fibonacci numbers.

num = int(input("Enter the value of N to generate its Fibonacci numbers:"))
a, b = 0, 1
print("The first", num, "Fibonacci numbers are:")
for i in range(num):
    print(a, end=' ')
    a, b = b, a + b

# 5)Check if a number is prime.

num = int(input("Enter the number: "))
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(num, "is not a prime number.")
        break
else:
    print(num, "is a prime number.")

# 6)Reverse a number (e.g., 123 → 321).

num = input("Enter a number to reverse:")
rev = " "

for i in num:
    rev = i + rev
print("The reversed number is:", rev)

# 7)Count digits in a number.

num = input("Enter a number to count its digits:")
count = 0
for i in num:
    count += 1
print("The number of digits in the number is:", count)

# 8)Find sum of even numbers between 1–100.

sum = 0
for i in range(2, 101, 2):
    sum += i
print("The sum of even numbers between 1-100 is:", sum)

# 9)Print a pyramid pattern

rows = int(input("Enter the number of rows for the pyramid: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

# 10)Find all divisors of a number.

num = int(input("Enter a number to find its divisors:"))
print("The divisors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)