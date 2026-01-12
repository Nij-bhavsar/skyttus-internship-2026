# 1) Create a dictionary storing student names and marks.

dict_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
print("Student marks dictionary:", dict_students)

# 2)Add a new key-value pair to an existing dictionary.

dict_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
dict_students["Om"] = 24
print("Updated dictionary with new student:", dict_students)

# 3)Delete a key-value pair from a dictionary.

dict_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
del dict_students["Het"]
print("The dictionary after remove one key-value pair", dict_students)

# 4) Merge two dictionaries into one.

dict1_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
dict2_students = {"jil":76, "Jay":70, "Yash":69, "Jeet":85, "Krit":72}

dic = dict1_students | dict2_students
print("The merged dictionary is:", dic)

# 5)Check if a key exists in a dictionary.

dict_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
key = "jil"

if key in dict_students:
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.")

# 6) Count word frequency in a given string using a dictionary.

string = "I am Nij Bhavsar and I am from Navsari"
word_list = string.split()
word_freq = {}
for word in word_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word frequency dictionary:", word_freq)

# 7) Find the key with the maximum value in a dictionary.

dict_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
max_key = max(dict_students, key=dict_students.get)
print(f"The student with the highest marks is: {max_key} with marks {dict_students[max_key]}")

# 8)Reverse keys and values in a dictionary.

dict_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
reversed_dict = {value: key for key, value in dict_students.items()}

print("The reversed dictionary is:", reversed_dict)

# 9)Update the value for a specific key.

dict_students = {"Nij":76, "Sanjay":70, "Meet":69, "Drish":85, "Het":72}
dict_students["Nij"] = 99

print("The Updated dictionary is:", dict_students)

# 10) Convert a list of tuples into a dictionary.

tuple_list = [("Nij", 76), ("Sanjay", 70), ("Meet", 69), ("Drish", 85), ("Het", 72)]
dict_from_tuples = dict(tuple_list)
print("Dictionary from list of tuples:", dict_from_tuples)




