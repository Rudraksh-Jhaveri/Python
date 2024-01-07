# Exercises: Level 1 Tuples (Rudraksh Jhaveri [D23CE164])

# 1. Create an empty tuple
empty_tuple = ()
print("Empty Tuple :", empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ('Harsh','Vijay','Meet','Rakesh','Salman')

sisters = ('Emma','Ava','Sofia','Wanda','Aria')

print("\nBrothers : ", brothers ,"\nSisters : ", sisters)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = (brothers + sisters)
print("\nSiblings : ",siblings)

# 4. How many siblings do you have?
length_siblings = len(siblings)
print("\nThere are",length_siblings,"siblings.")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.insert(0,'Elizabeth')
siblings.insert(0,'Chris')
family_members = tuple(siblings)
print("\nFamily Member :",family_members)