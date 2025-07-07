# level 1:
for i in range(1, 11):
    print(i)

while i <= 10:
    print(i)
    i += 1

for i in range(10, 0, -1):
    print(i)

while i >= 1 and i <= 10:
    print(i)
    i -= 1

for i in range(1, 8):
    print('#' * i)

for i in range(8):  # 8 rows
    for j in range(8):  # 8 columns
        print('#', end=' ') # end=' ' keeps the output on the same line.
    print()  # Move to the next line after each row. print() function by default ends with a newline (\n).

for i in range(11):
    print(f'{i} x {i} = {i * i}') # prints the square of each number from 0 to 10

it_languages = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for i in range(len(it_languages)):
    print(it_languages[i]) # prints the list of IT languages

for i in range(101):
    if i % 2 == 0:
        print(i) # prints even numbers from 0 to 100

for i in range(101):
    if i % 2 != 0:
        print(i) # prints odd numbers from 0 to 100

# Level 2:
total = 0
for i in range(1, 101):
    total += i # adds each number from 1 to 100 to the total
print(f'The sum of all numbers from 1 to 100 is {total}') # prints the total sum

total_even = 0
total_odd = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_even += i # adds each even number from 1 to 100 to the total_even
    else:
        total_odd += i # adds each odd number from 1 to 100 to the total_odd
print(f'The sum of all even numbers from 1 to 100 is {total_even}') # prints the total sum of even numbers
print(f'The sum of all odd numbers from 1 to 100 is {total_odd}') # prints the total sum of odd numbers


# level 3:
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries import countries
print(countries)  # ['Afghanistan', 'Albania', 'Algeria', ...]
print(len(countries))  # 195

# Filter countries containing 'land'
land_countries = []

for country in countries:
    if 'land' in country:
        land_countries.append(country)

print("Countries containing 'land':", land_countries)

#shortcut:
print("Countries containing 'land': ", [country for country in countries if 'land' in country])

# reverse the order of list:
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print(fruit)

# countries:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data
print(countries_data)

# Get all unique languages from countries_data
all_languages = set()
for country in countries_data:
    for lang in country['languages']:
        all_languages.add(lang)
print("Total number of unique languages:", len(all_languages))

# 10 most spoken languages:
from collections import Counter # counts the occurrences of each element in an iterable
language_counter = Counter()
for country in countries_data:
    for lang in country['languages']:
        language_counter[lang] += 1
most_common_languages = language_counter.most_common(10)

# 10 most populated countries:
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("10 most populated countries:")
# lambda x: x['population'] is an anonymous function that takes a country dictionary x and returns its population.

for country in sorted_countries[:10]:
    print(f"{country['name']}: {country['population']}")


# lambda in Python is a way to create a small, anonymous function (a function without a name) in a single line.
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
