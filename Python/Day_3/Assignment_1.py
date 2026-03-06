# #String
# # 1)Print the length of the string.

# string = input("Enter your String:")
# print(len(string))

# # 2)Convert the line into lowercase and uppercase.

# sentence = input("Enter a sentence: ")
# print(sentence.lower())
# print(sentence.upper())

# # 3)Replace spaces with underscores in a string.

# Text = input("Enter your text:")
# modified_text = Text.replace(" ", "_")
# print(modified_text)

# # 4)Extract the first and last character of a string.

# s1 = input("Enter your string:")

# print("First character:", s1[0])
# print("Last character:", s1[-1])

# # 5) Reverse a string using slicing.

# string = input("Enter Your string:")
# print("Reverse string is:", string[::-1])

# # 6)Count how many times a letter appears in a string.

# string = input("Enter the string:").lower()
# letter = input("Enter the word:").lower()
# count = string.count(letter)
# print(f"The word {letter} appears {count} times in the string.")

# # 7) Check if a word is present in a sentence.

# str = input("Enter your sentence:").lower()
# word = input("Enter the word:").lower()
# if word in str:
#     print(f"{word} is present in the sentence.")
# else:
#     print(f"{word} is not present in the sentence.")

# # 8)Take name & age and print using f-string formatting.

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(f"My name is {name} and I am {age} years old.")

# # 9)Remove extra spaces from the start and end of a string.

# string = input("Enter the string:")
# print("Trimmed string:", string.strip())

# # 10)Join a list of words into a single string with - between them.

# words = input("Enter your words:")
# split_words = words.split()
# joined_string = "-".join(split_words)
# print(joined_string)

# # List
# # 1) Create a list of your 5 favorite movies.
# fav_movies = input("Enter the movies:").split()
# print("My favorite movies are:", fav_movies)

# # 2) Add a new movie to the list.

# fav_movies = ["Deva", "Sikandar", "Leo", "S3", "Animal"]
# add = input("Enter the movies:")
# fav_movies.append(add)
# print("Updated movie list:", fav_movies)

# # 3) Remove the first movie from the list.

# fav_movies = ["Deva", "Sikandar", "Leo", "S3", "Animal"]
# rm = input("Enter the movie that you want to remove:")
# fav_movies.remove(rm)
# print("After removing the movie:", fav_movies)

# # 4)Sort a list of numbers in ascending order.

# numbers = list(map(int, input("Enter the numbers:").split()))
# numbers.sort()
# print("Sorted numbers in ascending order:", numbers)

# # 5)Reverse a list.

# num = [7, 8, 9, 10, 11]
# num.reverse()
# print("Reversed list:", num)

# # 6) Find the largest number in a list.

# num = [100, 234, 980, 12, 10]
# print("The largest number is:", max(num))

# # 7) Merge two lists into one.

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# merged_list = l1 + l2
# print("Merged list:", merged_list)

# # 8) Access the last element of a list without using index number.

# my_list = ['apple', 'banana', 'cherry', 'orange']
# last_element = my_list.pop()
# print("Last element:", last_element)

# # 9)Create a nested list and access a specific inner element.

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Accessing the element at index [1][2]:", nested_list[1][2])

# # 10)Count how many times an element appears in a list.

# list_1 = [1, 23, 3, 4, 23, 5, 23]
# element = 23
# count = list_1.count(element)
# print(f"The element '{element}' appears {count} times in the list.")