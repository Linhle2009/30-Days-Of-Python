lst = []
social_media = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat', 'TikTok']
print(len(social_media))  # 6
first_item = social_media[0]
last_item = social_media[-1]
middle_item = social_media[2]

mixed_data_types = ['John', 30, 1.75, True, 'New York']

it_companies = ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies) 
print(len(it_companies))  # 6
print(it_companies[0])  # Google
print(it_companies[-1])  # Amazon
print(it_companies[2])  # Apple
it_companies.append('Facebook')
it_companies.insert(2, 'Twitter')
print(it_companies)  # ['Google', 'Microsoft', 'Twitter', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Facebook']

it_companies[0] = it_companies[0].upper()
print(it_companies)  # ['GOOGLE', 'Microsoft', 'Twitter', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Facebook']

it_companies_new = it_companies +  ['#;  ']
print(it_companies_new)  # ['GOOGLE', 'Microsoft', 'Twitter', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Facebook', '#;  ']

does_exist = 'Google' in it_companies
print(does_exist)  # True
does_exist = 'Facebook' in it_companies
print(does_exist)  # True

it_companies = ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)  # ['Amazon', 'Apple', 'Google', 'IBM', 'Microsoft', 'Oracle']

it_companies.reverse()
print(it_companies)  # ['Oracle', 'Microsoft', 'IBM', 'Google', 'Apple', 'Amazon']

it_companies = ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies[0:3])  # ['Google', 'Microsoft', 'Apple']
print(it_companies[-4:-1])  # ['IBM', 'Oracle', 'Amazon']
print(it_companies[2:4])  # ['Apple', 'IBM']
del it_companies[0]
print(it_companies)  # ['Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[2] # removing IBM
print(it_companies)  # ['Microsoft', 'Apple', 'Oracle', 'Amazon']
it_companies.pop()  # removing the last item
print(it_companies)  # ['Microsoft', 'Apple', 'Oracle']
it_companies.clear()  # clearing the list
print(it_companies)  # []
del it_companies # it_companies is now empty
print(it_companies)  # NameError: name 'it_companies' is not defined


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack_copy = full_stack.copy()
print(full_stack_copy)  # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack_copy.insert(5, 'Python')
full_stack_copy.insert(6, 'SQL')
print(full_stack_copy)  # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python SQL', 'Node', 'Express', 'MongoDB']

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
min_age = min(ages)
max_age = max(ages) 
median_age = ages[len(ages) // 2] if len(ages) % 2 != 0 else (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
print(min_age)  # 19
average_age = sum(ages) / len(ages)
print(average_age)  # 22.4
range_age = max_age - min_age
print(range_age)  # 7

min_avg_age = min_age - average_age
max_avg_age = max_age - average_age
abs_min_avg_age = abs(min_avg_age)
abs_max_avg_age = abs(max_avg_age)
print(abs_min_avg_age, abs_max_avg_age)

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries import countries
print(countries)  # ['Afghanistan', 'Albania', 'Algeria', ...]
print(len(countries))  # 195

middle_index = len(countries) // 2
print("Middle country:", countries[middle_index])

first_half = countries[:middle_index]
second_half = countries[middle_index:]
print("First half of countries:", first_half)
print("Second half of countries:", second_half)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries
print("First country:", first)  # China
print("Second country:", second)  # Russia
print("Third country:", third)  # USA
print("Scandic countries:", *scandic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark']