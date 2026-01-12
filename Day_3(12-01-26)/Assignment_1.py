# 1)Print the length of the string.

string = "Nij Bhavsar"
print(len(string))

# 2)Convert the line into lowecase.

sentence = input("Enter a sentence: ")
print(sentence.lower())

# 3)Replace spaces with underscores in a string.

text = "Hello World! Welcome to Python Programming."
modified_text = text.replace(" ", "_")
print(modified_text)

# 4)Extract the first and last character of a string.

s1 = "BHAVSAR"

first_char_s1 = s1[0]
last_char_s1 = s1[-1]

print("First character:", first_char_s1)
print("Last character:", last_char_s1)

# 5) Reverse a string using slicing.

string = "nij bhavsar"
reversed_string = string[::-1]
print(reversed_string)

# 6)Count how many times A letter appears in a string.

string = "I am learning Python programming"
letter = "a"
count = string.count(letter)
print(f"The letter '{letter}' appears {count} times in the string.")

# 7) Check if a word is present in a sentence.

str = "I am curently persuing my B.E. in CSE"
word = "B.E."
if word in str:
    print(f"The word '{word}' is present in the sentence.")
else:
    print(f"The word '{word}' is not present in the sentence.")

# 8)Take name & age and print using f-string formatting.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"My name is {name} and I am {age} years old.")

# 9)Remove extra spaces from the start and end of a string.

string = "   Pratapnagar   "
trimmed_string = string.strip()
print("Trimmed string:", trimmed_string)

# 10)Join a list of words into a single string with - between them.

words = ["This", "is", "Volkswagen", "Virtus", "GT"]
joined_string = "-".join(words)
print(joined_string)