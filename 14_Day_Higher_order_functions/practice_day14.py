### Level 1:
# map: Transform each item. (One-to-one, same size output)
# filter: Select items based on a condition. (One-to-many/few, smaller or same size output)
# reduce: Combine all items into a single result. (Many-to-one, single value output)

# Higher-Order Function (HOF): A function that either takes one or more functions as arguments, or returns a function as its result (or both).
# -->Example: map(), filter(), sorted(key=...).
# Closure:  A nested function that "remembers" and can access variables from its enclosing (outer) scope, even after the outer function has finished executing.
# --> Example: In def outer(): x=10; def inner(): return x; return inner, the inner function is a closure because it "remembers" x=10.
# Decorator: takes a function as input and returns a new function that usually "wraps" or enhances the original function without directly modifying its source code.
# --> Example: The @my_decorator syntax above a function definition.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)


### Level 2:
# Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

countries_upper = map(lambda country: country.upper(), countries)
print(list(countries_upper)) # we need to print list here as map is the higher order function which returns a function

def change_to_upper(name):
    return name.upper()
name_upper = map(change_to_upper, countries)
print(list(name_upper))

# Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = map(lambda x: x**2, numbers)
print(list(square))

def square_num(x):
    return x**2
square_num_list = map(square_num, numbers)
print(list(square_num_list))

#Use map to change each name to uppercase in the names list:
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

names_upper = map(lambda name: name.upper(), names)
print(list(names_upper))

# Use filter to filter out countries containing 'land':
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def has_land(country):
    if 'land' in country:
        return True
    return False
has_land_countries = filter(has_land, countries)
print(list(has_land_countries))


#Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six_char(country):
    if len(country) == 6:
        return True
    return False
six_char_countries = filter(six_char, countries)
print(list(six_char_countries))


# Use filter to filter out countries containing six letters and more in the country list:
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Laos']
def six_char(country):
    if len(country) >= 6:
        return True
    return False
six_char_countries = filter(six_char, countries)
print(list(six_char_countries))


# Use filter to filter out countries starting with an 'E':
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Laos']

start_e = filter(lambda country: country.startswith('E'), countries)
print(list(start_e))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback)):
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Chained operations
# 1. map(lambda x: x * x, numbers)          -> Returns iterator of squared numbers
# 2. filter(lambda x: x % 2 == 0, ...)      -> Takes squared numbers, returns iterator of even squared numbers
# 3. reduce(lambda x, y: x + y, ...)        -> Takes even squared numbers, returns their sum

final_result_chained = reduce(
    lambda x, y: x + y,                          # The reduce function
    filter(                                      # The filter operation
        lambda x: x % 2 == 0,                    #   - filter condition
        map(lambda x: x * x, numbers)            # The map operation
    )
)
print(f"\nFinal result (chained): {final_result_chained}")
# Output: Final result (chained): 220


# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
mix = ['Asabeneh', 2, 'Lidiya', 5, 'Ermias', 9, 3, 'Abraham']

def get_string_lists(list):
    string_list = [item for item in list if type(item) == str]
    return string_list
print(get_string_lists(mix))

# Use reduce to sum all the numbers in the numbers list.:
from functools import reduce
mix = ['Asabeneh', 2, 'Lidiya', 5, 'Ermias', 9, 3, 'Abraham']

# Correct lambda for reduce: (accumulator, current_item)
# Use isinstance() for more robust type checking
sum_of_numbers = reduce(
    lambda acc, item: acc + item 
    if isinstance(item, int) else acc, # If the item is an integer, add it to acc.
    mix, # The iterable to process
    0    # The initial value for the accumulator (acc starts at 0)
)
print(sum_of_numbers)
# Expected Output: Sum of numbers using reduce: 19

# another way:
from functools import reduce
mix = ['Asabeneh', 2, 'Lidiya', 5, 'Ermias', 9, 3, 'Abraham']

# Define a function that accepts two arguments for 'reduce'
def add_if_integer(accumulator, current_item):
    if isinstance(current_item, int):
        return accumulator + current_item
    else:
        return accumulator # If it's not an int, just return the accumulator unchanged

# the function you pass to reduce() (in this case, add_if_integer) must be a binary function (it needs to accept exactly two arguments).
# reduce work by trying to take 2 arguements, so the function defines must also design to take 2 arguments, like x+y
sum_of_int = reduce(add_if_integer, mix, 0) #like here it takes the first 2 items 'Asabeneh', 2, and then run through the function add_if_interger, in this case:
# 1 : The accumulator (the running result of the reduction so far).
# 2 : The current item from the iterable being processed.
# remember to add 0 which is like initial number. It explicitly sets the starting point of your accumulation.
print(sum_of_int)


# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
connect = reduce(lambda x, y: x + ", " + y, countries[:-1])
# Now, complete the sentence
last_country = countries[-1] # Get the last country: 'Iceland'
# Combine everything
final_sentence = f"{connect}, and {last_country} are north European countries"
print(final_sentence)


# Declare a function called categorize_countries that returns a list of countries with some common pattern 
# (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')):
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries import countries
print(countries)  # ['Afghanistan', 'Albania', 'Algeria', ...]

def categorize_countries(pattern, country_name):
    return pattern in country_name # Returns True/False directly

has_land_countries = filter(lambda country: categorize_countries('land', country), countries)
print(list(has_land_countries)) # returns all land countries

has_ia_countries = filter(lambda country: categorize_countries('ia', country), countries)
print(list(has_ia_countries))


# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.:
import sys
import os
from functools import reduce
from collections import defaultdict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries import countries
print(countries)  # ['Afghanistan', 'Albania', 'Algeria', ...]

    # Define the reduction function (can be a lambda or a def function)
    # This function takes the accumulator (the dictionary being built)
    # and the current item (a country name)
def update_counts(counts_dict, country):
    first_letter = country[0].upper()
    counts_dict[first_letter] += 1 # Increment the count using defaultdict's default of 0
    return counts_dict # Always return the updated accumulator (the dictionary)
letter = reduce(update_counts, countries, defaultdict(int))
    # Use reduce to apply the update_counts function cumulatively
    # The initial value for the accumulator is a defaultdict(int), which automatically
    # creates new keys with a default value of 0 when first accessed.
print(letter)
print(dict(letter))


# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.:
import sys
import os
from functools import reduce
from collections import defaultdict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries import countries
print(countries)  # ['Afghanistan', 'Albania', 'Algeria', ...]

def get_first_ten_countries(list):
    return list[:10] # This slice gets items from index 0 up to (but not including) 10
print(get_first_ten_countries(countries))

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(list):
    return list[-10:] ## This slice gets items from the 10th-to-last up to the end
print(get_last_ten_countries(countries))


### LEvel 3: 
import sys
import os
from collections import Counter # counts the occurrences of each element in an iterable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data
print(countries_data)

# 1. Sort countries by name, by capital, by population:
countries_by_name = sorted(countries_data, key=lambda country: country['name'])
print(countries_by_name)

countries_by_capital = sorted(countries_data, key = lambda country: country['capital'])
coountries_by_population = sorted(countries_data, key = lambda country: country['population'])

# 2. Sort out the ten most spoken languages by location:
import sys
import os
from collections import Counter # counts the occurrences of each element in an iterable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data
# This requires collecting all languages from all countries, counting their occurrences, and then finding the top 10.
all_languages = []
for country in countries_data:
    # Extend the list with all languages spoken in the current country
    all_languages.extend(country['languages']) # Adds all individual items from an iterable (like another list, tuple, or string) to the end of the list.
    # different from append:If that element is itself another list, append will add that entire list as a single item to the main list. It does not unpack the inner list.

# Use collections.Counter to count the occurrences of each language
language_counts = Counter(all_languages)

# Get the ten most common languages
most_spoken_languages = language_counts.most_common(10)

print("\nTen Most Spoken Languages:")
for i, (language, count) in enumerate(most_spoken_languages):
    print(f"{i+1}. {language}: {count} countries")


# 3. Sort out the ten most populated countries.
# Sort by Population in descending order (largest first)
# Use reverse=True to sort from largest to smallest
import sys
import os
from collections import Counter # counts the occurrences of each element in an iterable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data
countries_by_population_desc = sorted(countries_data, key=lambda country: country['population'], reverse=True)

# Get the top 10 most populated countries by slicing
most_populated_countries = countries_by_population_desc[:10]
print(most_populated_countries)

print("\nTen Most Populated Countries:")
for i, country in enumerate(most_populated_countries): 
    #enumerate(iterable, start=0) takes an iterable (like a list) and an optional start index. It returns an iterator that yields tuples of (counter, value)
    print(f"{i+1}. {country['name']}: {country['population']:,} people")

# Example output might look like:
# 1. China: 1,379,302,771 people