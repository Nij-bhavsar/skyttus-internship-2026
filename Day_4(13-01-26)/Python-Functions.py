# 1) Function to check if a number is prime.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("It is Prime number.")
else:
    print("It is Not a prime number.!!")

# 2)Function to reverse a string.

def reversed(n):
    return n[::-1]

string = input("Enter your string: ")
print("The reversed string is:", reversed(string))

# 3)Function to find factorial.

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input("Enter a number:"))
print("The factorial of", num, "is", fact(num))

# 4)Function to calculate simple interest

def simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))

si = simple_interest(p, r, t)
print("The Simple Interest is:", si)

# 5)Function to check if a word is palindrome.

def pallindrome(word):
    return word == word[::-1]

word = input("Enter your word:")
if pallindrome(word):
    print("It is a Pallindrome!!!.")

else:
    print("It is Not a Pallindrome!.")

# 6)Function to count vowels in a string.

def vowel_c(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter your string:")
print("The number of vowels in the string is:", vowel_c(string))

# 7)Function to merge two lists.

def merge_list(l1, l2):
    return l1 + l2

l1 = [11, 12, 13]
l2 = [14, 15, 16]

merged = merge_list(l1, l2)
print("The merged list is:", merged)

# 8)Function to find GCD of two numbers.

def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
print("The GCD of", n, "and", m, "is:", gcd(n, m))

# 9)Function to find area of rectangle.

def ar_rec(l, b):
    return l * b

l = float(input("Enter the length of a rectangle:"))
b = float(input("Enter the breadth of a rectangle:"))
print("The are of a rectangle is:", ar_rec(l, b))

# 10)Function to check Armstrong number.

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    return total == num

number = int(input("Enter your number: "))

if is_armstrong(number):
    print(f"This {number} is an Armstrong number")
else:
    print(f"This {number} is not an Armstrong number")