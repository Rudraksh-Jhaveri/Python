# Dictionaries Exercises
# 1. Create  an empty dictionary called dog
dog = {}
print("Empty Dictionary Dog :", dog)

# 2. Add name, color, breed, legs, age to the dog dictionary

dog = {
    'Name': 'Sheru',
    'Breeds': 'Bulldog',
    'Legs': 4,
    'Age': 5
}

print("\nDog Dictionary :", dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 18,
    'marital_status': 'Single',
    'skills': ['Programming', 'Problem Solving', 'Communication'],
    'country': 'United States',
    'city': 'New York',
    'address': '123 Main Street'
}
print("\nStudent dictionary : ",student_dict)

# 4. Get the length of the student dictionary
student_len = len(student_dict)
print("\nLength of Student dictionary :", student_len)

# 5. Get the value of skills and check the data type, it should be a list
skills_value = student_dict['skills']

print("\nValue of skills :", skills_value)
print("Type of skills value :", type(skills_value))

# 6. Modify the skills values by adding one or two skills
skills_value.append('Critical Thinking')
skills_value.append('Teamwork')
print("\nModify the skills value :", skills_value)

# 7. Get the dictionary keys as a list
keys_list = student_dict.keys()
print("\nDictionary keys as a list :", keys_list)

# 8. Get the dictionary values as a list
key_value = student_dict.values()
print("\nDictionary values as a list :", key_value)

# 9. Change the dictionary to a list of tuples using _items()_ method
print("\nDictionary to a list of tuples :", student_dict.items())

# 10. Delete one of the items in the dictionary
print("\nDelete One item :", student_dict.popitem())
print("\n",student_dict)
# 11. Delete one of the dictionaries
del dog
print("\nDelete Dog Dictionaries.")
