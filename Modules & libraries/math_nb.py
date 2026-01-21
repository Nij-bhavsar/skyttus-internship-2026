# Create a custom math module and import it in another file.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a/b  

# Create a module to perform string operations.
def to_upper(text):
    return text.upper()
def to_lower(text):
    return text.lower()
def reverse_string(text):
    return text[::-1]
def count_vowel(text):
    vowel="aeiouAEIOU"
    count=0
    for ch in text:
        if ch in vowel:
            count +=1
    return count
def is_palindrom(text):
    text =text.lower().replace(" ","")
    return text == text[::-1]

# Use random module to generate 5 random integers.
import random
for i in range(5):
    num=random.randint(1,100)
    print(num)

# Use datetime module to display current date and time.
from datetime import datetime
now=datetime.now()
print(now)
from datetime import datetime
now=datetime.now()
print("Date:",now.strftime("%d-%m-%Y"))
print("Time:",now.strftime("%H-%M-%S"))

# Use math module to find factorial of a number.
import math
num=int(input("Enter a number:"))
result=math.factorial(num)
print("Factorial:",num,"is",result)

# Create a package shapes with modules for circle and rectangle.
import math
def area(radius):
    return math.pi*radius*radius
def circumference(radius):
    return 2*math.pi*radius

def area1(lenght,width):
    return lenght*width
def parimeter(lenght,width):
    return 2* (lenght+width)

# Import multiple functions from one module and use them.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a/b  

# Write a program to shuffle a list using random module.
import random
numbers=[33,29,25,129,45,125]
print("Organized_list:",numbers)
random.shuffle(numbers)
print("Shuffle:",numbers)

# Write a program to calculate the difference between two dates.
from datetime import date
date1=date(2004,10,10)
date2=date(2005,5,23)
difference=date2-date1
print("Difference in days:",difference.days)

# Use os module to list files in a directory.
import os
path="."
items=os.listdir(path)
for item in items:
    print(item)