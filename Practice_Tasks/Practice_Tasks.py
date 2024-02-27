# Task 1: Reverse the given string
name = "Rudraksh"
reversed_name = name[::-1]
print("Reversed string:", reversed_name)

# Task 2: Replace some character of the string
replaced_name = name.replace('u', 'x')
print("String with replaced characters:", replaced_name)

# Task 3: Find whether the character is in the string
char_to_find = 'a'
if char_to_find in name:
    print(f"'{char_to_find}' is in the string.")
else:
    print(f"'{char_to_find}' is not in the string.")

# Task 4: Create tuple, list, and set
my_tuple = tuple(name)
my_list = list(name)
my_set = set(name)
print("Tuple:", my_tuple)
print("List:", my_list)
print("Set:", my_set)

# Task 5: Convert string characters to upper and lower case and split
upper_case = name.upper()
lower_case = name.lower()
split_string = name.split('u')
print("Uppercase:", upper_case)
print("Lowercase:", lower_case)
print("Split:", split_string)

# Task 6: Operations on tuple and list
my_tuple = (5, 2, 8, 1, 9)
my_list = [5, 2, 8, 1, 9]
print("Tuple - Max:", max(my_tuple), "Min:", min(my_tuple), "Length:", len(my_tuple), "Sum:", sum(my_tuple))
print("List - Max:", max(my_list), "Min:", min(my_list), "Length:", len(my_list), "Sum:", sum(my_list))

# Task 7: Copy list without using copy command
list1 = [1, 2, 3, 4, 5]
list2 = list1[:]

# Task 8: Dictionary operations
student = {'name': 'Rudraksh', 'age': 20, 'grade': 'A'}
print("Age:", student['age'])
student['grade'] = 'B'
if 'gender' in student:
    print("Gender is present.")
else:
    print("Gender is not present.")

# Task 9: Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Is set1 subset of set2:", set1.issubset(set2))

# Task 10: Dictionary with sets
subjects = {'math': {'Alice', 'Bob'}, 'science': {'Charlie', 'David'}}
subjects['math'].add('Eve')
subjects['science'].remove('Charlie')
print("Common students:", subjects['math'].intersection(subjects['science']))

# Task 11: Lists with elements at even and odd indices
original_list = [1, 2, 3, 4, 5, 6]
even_indices = original_list[::2]
odd_indices = original_list[1::2]
print("Even indices:", even_indices)
print("Odd indices:", odd_indices)

# Task 12: Swap values using tuple packing/unpacking
a = 5
b = 10
a, b = b, a
print("a:", a, "b:", b)

# Task 13: Check if list is a palindrome
def is_palindrome(lst):
    return lst == lst[::-1]

print("Is [1, 2, 3, 2, 1] a palindrome?", is_palindrome([1, 2, 3, 2, 1]))

# Task 14: Concatenate two tuples without using +
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)