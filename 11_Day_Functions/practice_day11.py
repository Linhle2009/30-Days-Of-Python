# level 1:
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

def area_of_circle(r):
    pi = 3.14
    area = pi * r ** r
    return area
print(area_of_circle(3))

def add_all_nums(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"In valid item: {arg} is not a number"
        total += arg 
    return total 
print(add_all_nums(3, 5.4, 'name'))
print(add_all_nums(5, 9, 10))

def convert_celsius_to_fahrenheit(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f
print(convert_celsius_to_fahrenheit(80))


def check_season(month):
    if month in [9, 10, 11]:
        return 'Autumn'
    elif month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Invalid month value'
print(check_season(3))
    
def calculate_slop(x1, y1, x2, y2):
    if x2 == x1:
        return 'Undefined slope (verticle line)'
    return (y2 - y1)/(x2 - x1)
print(calculate_slop(x1 = 5, x2 = 9, y1 = 8, y2 = 3))

import numpy as np # to solve equation
def solve_quadric_eqn(a, b, c):
    coefficients = [a, b, c]
    roots = np.roots(coefficients)
    return roots 
print(solve_quadric_eqn(2, 4, 1))

def print_list(list):
    for item in list:
        print(item)
fruits = ['apple', 'banana', 'cherry', 'date']
print_list(fruits)
    
def reverse_list(list):
    list_reverse = []
    for index in range(len(list) - 1, -1, -1): #start, stop, step
        list_reverse.append(list[index])
    print(list_reverse)
fruits = ['apple', 'banana', 'cherry', 'date']
reverse_list(fruits)

def capitalized_list_items(list):
    list_capital = []
    for item in list:
        list_capital.append(item.capitalize())
    print(list_capital)
fruits = ['apple', 'banana', 'cherry', 'date']
capitalized_list_items(fruits)

def add_item(list, para):
    list.append(para)
    return list
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 

def remove_item(list, para):
    list.remove(para)
    return list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(number):
    total = 0
    for n in range(number + 1):
        total += n
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(number):
    total_odd = 0
    for n in range(number + 1):
        total_odd += n if n % 2 == 1 else 0
    return total_odd
print(sum_of_odds(5))  
print(sum_of_odds(10)) 
print(sum_of_odds(100)) 

def sum_of_odds(number):
    return sum(n for n in range(number + 1) if n % 2 == 1)

def sum_of_even(number):
    return sum(n for n in range(number + 1) if n % 2 == 0)
print(sum_of_even(5))  
print(sum_of_even(10)) 
print(sum_of_even(100)) 

# level 2:
def evens_and_odds(number):
    evens = 0
    odds = 0
    for n in range(number + 1):
        evens += 1 if n % 2 == 0 else 0
        odds += 1 if n % 2 ==1 else 0
    return evens, odds
print(evens_and_odds(100))

def evens_and_odds(number):
    evens = sum(1 for n in range(number + 1) if n % 2 == 0)
    odds = sum(1 for n in range(number + 1) if n % 2 == 1)
    return evens, odds
print(evens_and_odds(100))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120


def is_empty(value): 
    return not value # not value returns True if the value is empty or False otherwise.

print(is_empty(""))        # True
print(is_empty([1, 2]))    # False
print(is_empty([]))        # True
print(is_empty(None))      # True
print(is_empty({}))        # True
print(is_empty("hello"))   # False


def calculate_mean(data):
    return sum(data) / len(data) if data else 0 #if data is not empty, else return 0
nums = [1, 2, 2, 3, 4, 5]
print('Mean', calculate_mean(nums))


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1], sorted_data[mid])
    else:
        return sorted_data[mid]
nums = [1, 2, 2, 3, 4, 5]
print('Median', calculate_median(nums))


from collections import Counter
def calculate_mode(data):
    if not data:
        return None
    freq = Counter(data) # Creates a frequency dictionary from the list. If data = [1, 2, 2, 3], then freq = {1: 1, 2: 2, 3: 1}
    max_count = max(freq.values()) # Finds the highest frequency value.
    modes = [k for k, v in freq.items() if v == max_count] # Give me a list of all the keys k from the dictionary freq where their value v equals the maximum count.
    return modes if len(modes) > 1 else modes[0] # If there’s more than one mode, return the whole list. If there’s just one, return it as a single number—more intuitive for users!
nums = [1, 2, 2, 3, 4, 5]
print("Mode:", calculate_mode(nums)) 

def calculate_range(data):
    return max(data) - min(data) if data else 0
nums = [1, 2, 2, 3, 4, 5]
print("Range", calculate_range(nums))


def calculate_variance(data):
    n = len(data)
    if n == 0:
        return 0
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / n
nums = [1, 2, 2, 3, 4, 5]
print("Variance:", calculate_variance(nums)) 

import math
def calculate_std(data):
    return math.sqrt(calculate_variance(data))
nums = [1, 2, 2, 3, 4, 5]
print("Std Dev:", calculate_std(nums))   


# Level 3:
def is_prime(num):
    if num == 0 or num == 1:
        print(num, 'is not prime number')
    elif num >1:
        for i in range(2, num):
            if num % i == 0:
                print(num, 'is not prime number')
                break
        else:
            print(num, 'is a prime number')
is_prime(5)
is_prime(16)


def check_unique_item(list):
    for item in list:
        print(item, 'Item is unique') if list.count(item) == 1 else print(item, 'Item is not unique')
print(check_unique_item([1, 2, 2, 4]))

def all_unique(items):
    return len(items) == len(set(items)) # If the length of the set matches the length of the original list, then all items were unique.
print(all_unique([1, 2, 3, 4]))      # True
print(all_unique([1, 2, 2, 4]))      # False
print(all_unique(["a", "b", "c"]))   # True
print(all_unique(["a", "b", "a"]))   # False

def same_type(items):
    return all(type(item) == type(items[0]) for item in items) 
#all(...) ensures that every item has that exact same type.
print(same_type([1, 2, 3]))          # True (all int)
print(same_type(["a", "b", "c"]))    # True (all str)
print(same_type([1, "2", 3]))        # False (mixed types)
print(same_type([]))                # True (empty list counts as same type)


import sys
import os
from collections import Counter # counts the occurrences of each element in an iterable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data
print(countries_data)

def most_spoken_language(dict):
    language_counter = Counter()
    for country in dict:
        for lang in country['languages']:
            language_counter[lang] += 1
    return language_counter.most_common(10)
print(most_spoken_language(countries_data))

def most_populated_countries(dict):
    sorted_countries = sorted(dict, key=lambda x: x['population'], reverse=True)
    return sorted_countries
print(most_populated_countries(countries_data))

