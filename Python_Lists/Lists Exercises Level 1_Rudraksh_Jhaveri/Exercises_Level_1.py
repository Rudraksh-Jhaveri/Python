# Exercises Level 1

# Rudraksh Jhaveri 

# 1. Declare an empty list
countries = []

# 2. Declare a list with more than 5 items
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
print("\nList of Countries : ", countries)

# 3. Find the length of your list
print("\nLength of a Countries : ", len(countries))

# To get the middle item of a list.
middle_index = (len(countries) //2)
middle_elements = countries[middle_index]

# 4. Get the first item, the middle item and the last item of the list
print("\nFirst Item : ", countries[0],"\n", "\nMiddle Item :", middle_elements,"\n", "\nLast Item : ", countries[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Rudraksh', 18, 162.56, 'Single', 'Jamnagar']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("\n")

# 7. Print the list using _print()_
print(mixed_data_types)
print("\n")
print(it_companies)

# 8. Print the number of companies in the list
print("\nNumber of compaines : ", len(it_companies))

# To get the middle item of a list.
middle_index = (len(it_companies) //2)
middle_elements = it_companies[middle_index]

# 9. Print the first, middle and last company
print("\nFirst Company : ", it_companies[0],"\n", "\nMiddle Company :", middle_elements,"\n", "\nLast Company : ", it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[-1] = 'Flipkart'
print("\nModify Amazon : ", it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Infosys')
print("\nAdd Infosys : ",it_companies)

# 12. Insert an IT company in the middle of the companies list
new_compaines = ['TCS']
it_companies = it_companies[:middle_index] + new_compaines + it_companies[middle_index:]
print("\nAdd TCS in middle :", it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)

company_to_change = 'Microsoft'

index_to_change = it_companies.index(company_to_change)

it_companies[index_to_change] = company_to_change.upper()

print("\nChange", company_to_change, "to uppercase", it_companies)

# 14. Join the it_companies with a string '#;&nbsp; '

print("\nAdd [#;&nbsp;] : ")
string = '#;&nbsp;'.join(it_companies)
print(string)

# 15. Check if a certain company exists in the it_companies list.
print("\n")
check_company = 'TCS'
check_company2 = 'Rudraksh Jhaveri'
index_to_check = it_companies.index(check_company)

if(index_to_change):
    print("Yes",check_company, "Company Exists.")

# 16. Sort the list using sort() method
it_companies.sort()
print("\nSort : ",it_companies)

# If we want to don't want to modify the original list.
# Then we can used 'sorted' built-in functions
# sorted_companies = sorted(it_companies)


# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse = True)
print("\nSort in Reverse : ",it_companies)

# 18. Slice out the first 3 companies from the list

first_3_compaines = it_companies[0:3]
print("\nFirst 3 Compaines of [Sort in Reverse] : ", first_3_compaines)

# 19. Slice out the last 3 companies from the list
first_3_compaines = it_companies[-3:]
print("\nLast 3 Compaines of [Sort in Reverse] : ", first_3_compaines)

# 20. Slice out the middle IT company or companies from the list
print("\n")
middle_company = (len(it_companies) // 2)
print("Middle Company or Companies : ", it_companies[middle_company])

# 21. Remove the first IT company from the list
print("\n")
it_companies.remove(it_companies[0])
print("Remove First Company: ", it_companies)

# 22. Remove the middle IT company or companies from the list
print("\n")
it_companies.pop(middle_company)
print("Middle Company Remove : ", it_companies)

# 23. Remove the last IT company from the list
print("\n")
del it_companies[-1]
print("Last Company Remove : ", it_companies)

# 24. Remove all IT companies from the list
print("\n")
# it_companies.clear()

#or using slice
remove_all_company = it_companies[:] = []

print("All Company Remove : ",it_companies)

# 25. Destroy the IT companies list
print("\n")
del it_companies[::]
print("Destroy it_compaines list.", it_companies)

# 26. Join the following lists:

#     ```py
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
#     ```
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

web_dev = front_end + back_end

# Or
front_end.extend(back_end)

print("\nJoin Two list : ",front_end)

full_stack = front_end.copy()

#insert python and sql.
full_stack.extend(['Python', 'SQL'])

print("\nCopy list in full_satck : ",full_stack)

