# 1) Create a tuple with 5 numbers.

num_tup = (11, 22, 33, 44, 55)
print("Tuple of numbers:", num_tup)

# 2)Access the third element in a tuple.

num_tup = (11, 22, 33, 44, 55)
third_element = num_tup[2]
print("The third element in the tuple is:", third_element)

# 3)Unpack a tuple into separate variables.

num_tup = (11, 22, 33)
a, b, c = num_tup
print("Unpacked values:", a, b, c)

# 4)Create a set of 5 fruits.

fruit_set = {"apple", "banana", "cherry", "guava", "strawberry"}
print("Set of fruits:", fruit_set)

# 5)Add a new fruit to the set.

fruit_set = {"apple", "banana", "cherry", "guava", "strawberry"}
fruit_set.add("orange")
print("Updated set of fruits:", fruit_set)

# 6)Remove an element from a set.

fruit_set = {"apple", "banana", "cherry", "guava", "strawberry"}
fruit_set.remove("banana")
print("Set after removing an element:", fruit_set)

# 7)Find union of two sets.

set1 = {7, 8, 9}
set2 = {2, 3, 4}

union_set = set1.union(set2)
print("Union of two sets:", union_set)

# 8)Find intersection of two sets.

set1 = {7, 8, 9, 10}
set2 = {9, 10, 11, 12}

intersection_set = set1.intersection(set2)
print("Intersection of two sets:", intersection_set)

# 9)Check if one set is subset of another.

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
subset_check = set2.issubset(set1)
print("Is set2 a subset of set1?>>", subset_check)

# 10)Convert a list with duplicate values into a set to remove duplicates.

num_list = [1, 2, 2, 3, 4, 4, 5]
num_set = set(num_list)
print("Set after removing duplicates:", num_set)

#Dictionary
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