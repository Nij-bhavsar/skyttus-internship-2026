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