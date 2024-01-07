# Exercises Level 2

# Rudraksh Jhaveri

# - Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print("Sorted Age : ", ages)

# find the min and max age
min_age = min(ages)
max_age = max(ages)

print("\nMinimum Age : ", min_age)
print("Maximum Age : ", max_age)

# - Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print("\nAdd Minimum and Maximum age :", ages)

# - Find the median age (one middle item or two middle items divided by two)
ages.sort()
length = len(ages)

if(length % 2 != 0):
    median_age = ages[length // 2]
else:
    median1 = ages[length // 2 - 1]
    median2 = ages[length // 2]
    median_age = (median1 + median2) / 2

print("\nSorted Age List : ",ages)
print("Median Age : ",median_age)

# - Find the average age (sum of all items divided by their number )
sum = 0
for n in ages:
    sum = sum + n

print("\nThe sum of age is :",sum)

average = (sum / length)
print("Average Age : ",average)

# - Find the range of the ages (max minus min)
ranges_of_age = max_age - min_age

print("\nRange of the ages :",ranges_of_age)

# - Compare the value of (min - average) and (max - average), use _abs()_ method

abs_diff_min = abs(min_age - average)
abs_diff_max = abs(max_age - average)

if abs_diff_min > abs_diff_max:
    print("\nAbsolute Difference (min - average) is greater.")
elif abs_diff_min < abs_diff_max:
    print("\nAbsolute Difference (max - average) is greater.")
else:
    print("\nAbsolute Differences are equal.")

print("\n")
print("\n")

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway','Denmark']
print("Countries List :", countries)

# 1. Find the middle country(ies) in the [countries list]

middle_countries = (len(countries) // 2)
length = len(countries)
print("\nMiddle Country :", countries[middle_countries])

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.

half_size = middle_countries // 2

if (length % 2 == 0):
    print("\nList is even [Total list in countries are :",length,"]")
    one_countries = countries[:middle_countries]
    two_countries = countries[middle_countries:]
    print("1st Country List :",one_countries)     
    print("2nd Country List :",two_countries)
else:
    print("\nList is odd [Total list in countries are :",length,"]")
    one_more_countries = countries[:half_size]
    one_countries = countries[half_size:middle_countries]
    two_countries = countries[middle_countries:]
    print("1st Country List :",one_more_countries)     
    print("2st Country List :",one_countries)     
    print("3rd Country List :",two_countries)


# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

first_three_countries = countries[:3]

Scandic_countries = countries[3:]

print("\nFirst Three Countries:",first_three_countries)
print("Scandic Countries:", Scandic_countries)