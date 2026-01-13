# 1)Write a program to read a file and display its contents.

file_name = 'nij.txt'
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found!!. Please check the file name and try again.")

# 2)Write a program to count the number of lines in a file.

file_name = 'nij.txt'
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print("Number of lines in the file:", len(lines))
except FileNotFoundError:
    print("Error: File not found!!. Please check the file name and try again.")

# 3)Write a program to count how many times each word appears in a file.

try:
    with open("nij.txt", "r") as file:
        text = file.read().lower()
        words = text.split()

        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        print("Word Frequency:")
        for word, count in word_count.items():
            print(word, ":", count)

except FileNotFoundError:
    print("Error: File not found")

# 4)Write a program to write 5 user-entered sentences to a file.

file_name = 'nij.txt'
with open(file_name, 'a') as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        file.write(sentence + '\n')
print(f"The 5 sentences have been written to {file_name}.")

# 5)Write a program to append a list of strings to an existing file.

strings_to_append = ["the_dr", "the_jd", "the_mp", "the_nb"]
file_name = 'nij1.txt'
with open(file_name, 'a') as file:
    for string in strings_to_append:
        file.write(string + '\n')
print(f"The list of strings has been appended to {file_name}.")

# 6)Write a program to read a file and print only lines containing a specific word.

try:
    specific_word = input("Enter the specific word to search for: ").lower()
    with open("nij1.txt", "r") as file:
        lines = file.readlines()

        print(f"Lines containing the word '{specific_word}':")
        for line in lines:
            if specific_word in line.lower():
                print(line.strip())
except FileNotFoundError:
    print("Error: File not found!!. Please check the file name and try again.")

# 7)Write a program to replace a specific word in a file and save changes.

try:
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")

    with open("nij1.txt", "r") as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open("nij1.txt", "w") as file:
        file.write(content)
    print("Word replaced successfully.")
except FileNotFoundError:
    print("Error: File not found")

# 8)Write a program to merge the contents of two text files into a third file.

try:
    with open("nij1.txt", "r") as f1, open("nij.txt", "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

    with open("merged.txt", "w") as f3:
        f3.write(content1)
        f3.write(content2)

    print("Files merged successfully into merged.txt")

except FileNotFoundError:
    print("Error: One of the files was not found")

# 9)Write a program to read a CSV file and display its content in a formatted way.

import csv
try:
    with open('pr1.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)

        print(f"{' | '.join(headers)}")
        print("-" * 40)

        for row in csvreader:
            print(f"{' | '.join(row)}")
except FileNotFoundError:
    print("Error: CSV file not found!!. Please check the file name and try again.")

# 10)Write a program to back up a file by copying its content into another file.

try:
    with open("nij1.txt", "r") as source_file:
        content = source_file.read()

    with open("nij.txt", "a") as backup_file:
        backup_file.write(content)

    print("File backup created successfully.")

except FileNotFoundError:
    print("Error: Original file not found.")