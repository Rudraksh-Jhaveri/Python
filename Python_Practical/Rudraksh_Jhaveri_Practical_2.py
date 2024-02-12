# A) Create a list and apply methods (append, extend, remove, reverse), arrange created list in ascending and descending order.
# Question: Create a list and apply methods (append, extend, remove, reverse), arrange created list in ascending and descending order.
# Solution:
my_list = [5, 2, 8, 3, 1]
print("Original list:", my_list)

# Append method
my_list.append(10)
print("After append:", my_list)

# Extend method
my_list.extend([6, 7])
print("After extend:", my_list)

# Remove method
my_list.remove(3)
print("After remove:", my_list)

# Reverse method
my_list.reverse()
print("After reverse:", my_list)

# Sorting in ascending order
my_list.sort()
print("Ascending order:", my_list)

# Sorting in descending order
my_list.sort(reverse=True)
print("Descending order:", my_list)

# B) List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
# From above list get word “orange” and “Python” & repeat this list five times without using loops.
# Question: From above list get word “orange” and “Python” & repeat this list five times without using loops.
# Solution:
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10, 20, 30]], 5, 6, 7, ["apple", "banana", "orange"]]
word_orange = List1[-1][-1]
word_python = List1[4][0]
result = [List1] * 5
print("Word 'orange':", word_orange)
print("Word 'Python':", word_python)
print("Repeated List:", result)

# C) Create a list and copy it using slice function
# Question: Create a list and copy it using slice function
# Solution:
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
print("Original List:", original_list)
print("Copied List:", copied_list)

# D) Create a tuple and apply different types of mathematical operations on it (Sum, Maximum, minimum etc.).
# Question: Create a tuple and apply different types of mathematical operations on it (Sum, Maximum, minimum etc.).
# Solution:
my_tuple = (5, 7, 3, 8, 2)
print("Tuple:", my_tuple)
print("Sum:", sum(my_tuple))
print("Maximum:", max(my_tuple))
print("Minimum:", min(my_tuple))