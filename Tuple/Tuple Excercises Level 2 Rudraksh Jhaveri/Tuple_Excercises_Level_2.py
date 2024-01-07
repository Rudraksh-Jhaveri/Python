# Exercises: Level 2 (Rudraksh Jhaveri [D23CE164])

# 1. Unpack siblings and parents from family_members
family_members = ('Chris', 'Elizabeth', 'Harsh', 'Vijay', 'Meet', 'Rakesh', 'Salman', 'Emma', 'Ava', 'Sofia', 'Wanda', 'Aria')
father, mother, *siblings = family_members

print("\nParents :", father,",",mother)
print("Siblings :", siblings)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Banana', 'Orange', 'Mango', 'Lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Milk', 'Meat', 'Butter', 'Yoghurt')

food_stuff_tp = (fruits + vegetables + animal_products)
print("\nFood_Stuff_Tuple :", food_stuff_tp)

# 3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("\nFood_Stuff_List :", food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = (len(food_stuff_lt) // 2)

# Using Slice
# middle_item = food_stuff_lt[6:7]
# print("\nMiddle Item :", middle_item)

print("\nMiddle Item :", food_stuff_lt[middle_index])

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

print("\nFirst Three Items :", first_three_items)
print("Last Three Items :", last_three_items)

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# If you call food_stuff_tp you will get NameError.
# print(food_stuff_tp)

# 7. Check if an item exists in  tuple:
# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

does_exist = 'Estonia' in nordic_countries
print("\nIs Estonia is a nordic country? - ", does_exist)

does_exist = 'Iceland' in nordic_countries
print("\nIs Iceland is a nordic country? - ",does_exist)
