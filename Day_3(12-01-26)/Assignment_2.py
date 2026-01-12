# 1) Create a list of your 5 favorite movies.
fav_movies = ["Deva", "Sikandar", "Leo", "S3", "Animal"]
print("My favorite movies are:", fav_movies)

# 2) Add a new movie to the list.

fav_movies = ["Deva", "Sikandar", "Leo", "S3", "Animal"]
fav_movies.append("Dhurandhar Part_1")
print("Updated movie list:", fav_movies)

# 3) Remove the first movie from the list.

fav_movies = ["Deva", "Sikandar", "Leo", "S3", "Animal"]
fav_movies.remove("Deva")
print("After removing the first movie:", fav_movies)

# 4)Sort a list of numbers in ascending order.

numbers = [23, 10, 5, 11, 21]
numbers.sort()
print("Sorted numbers in ascending order:", numbers)

# 5)Reverse a list.

num = [7, 8, 9, 10, 11]
num.reverse()
print("Reversed list:", num)

# 6) Find the largest number in a list.

num = [100, 234, 980, 12, 10]
print("The largest number is:", max(num))

# 7) Merge two lists into one.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
merged_list = l1 + l2
print("Merged list:", merged_list)

# 8) Access the last element of a list without using index number.

my_list = ['apple', 'banana', 'cherry', 'orange']
last_element = my_list.pop()
print("Last element:", last_element)

# 9)Create a nested list and access a specific inner element.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Accessing the element at index [1][2]:", nested_list[1][2])

# 10)Count how many times an element appears in a list.

list_1 = [1, 23, 3, 4, 23, 5, 23]
element = 23
count = list_1.count(element)
print(f"The element '{element}' appears {count} times in the list.")