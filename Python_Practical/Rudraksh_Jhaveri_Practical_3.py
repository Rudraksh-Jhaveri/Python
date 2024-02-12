
# Practical_3 

# A) String Operations:
#  Reverse a string, replace string with other string, merge two strings
#  Find character is in string or not without using loops
#  Split string into multiple words &characters

# Reverse a string
original_string = "hello"
reversed_string = original_string[::-1]
print(reversed_string)  # Output: "olleh"

# Replace string with another string
original_string = "hello world"
new_string = original_string.replace("world", "universe")
print(new_string)  # Output: "hello universe"

# Merge two strings
string1 = "hello"
string2 = "world"
merged_string = string1 + string2
print(merged_string)  # Output: "helloworld"

# Check if a character is in a string without using loops
char = "a"
string = "hello"
is_in_string = char in string
print(is_in_string)  # Output: False

# Split string into multiple words and characters
string = "hello world"
word_list = string.split()
character_list = list(string)
print(word_list)  # Output: ['hello', 'world']
print(character_list)  # Output: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# B) Dictionaries Operations:
#  Apply “Update, Delete, clear, popitem, pop, get, keys and values” operation in
# dictionary.
#  Create 3 dictionaries and merge them into 1 dictionary

# Create dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Merge dictionaries
merged_dict = {**dict1, **dict2, **dict3}
print("Merged dictionary:", merged_dict)

# Update dictionary
dict1.update({'b': 20, 'g': 7})
print("Updated dictionary:", dict1)

# Delete item from dictionary
del dict2['c']
print("Dictionary after deleting 'c':", dict2)

# Clear dictionary
dict3.clear()
print("Dictionary after clearing:", dict3)

# Pop an item from dictionary
pop_item = merged_dict.popitem()
print("Popped item:", pop_item)
print("Dictionary after popping:", merged_dict)

# Pop a specific item from dictionary
pop_value = merged_dict.pop('b')
print("Popped value:", pop_value)
print("Dictionary after popping 'b':", merged_dict)

# Get value from dictionary
value = merged_dict.get('a')
print("Value of 'a':", value)

# Get keys and values from dictionary
keys = merged_dict.keys()
values = merged_dict.values()
print("Keys:", keys)
print("Values:", values)

