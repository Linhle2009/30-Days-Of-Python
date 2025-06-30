print('Day 2: 30 Days of python programming')
first_name = 'Linh'
last_name = 'Le'
full_name = first_name + ' ' + last_name
country = 'Vietnam'
city = 'Hanoi'
age = 27
year = 2023
is_married = False
is_true = True
is_light_on = True
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = \
    'Linh', 'Le', 'Linh Le', 'Vietnam', 'Hanoi', 27, 2023, False, True, True

print(type(first_name))  # <class 'str'>
print(type(last_name))   # <class 'str'>    
print(type(full_name))   # <class 'str'>
print(type(country))     # <class 'str'>
print(type(city))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(year))        # <class 'int'>
print(type(is_married))  # <class 'bool'>       
print(type(is_true))     # <class 'bool'>
print(type(is_light_on)) # <class 'bool'>

print(len(first_name))  # 4
print(len(last_name))   # 2

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
remainder = num_one % num_two # 1 modulus division to get the remainder
floor_division = num_one // num_two # 1 floor division to get the quotient, rounding down to the nearest integer

radius = 30
area_of_circle = 3.14 * radius ** 2 # area of a circle
circum_of_circle = 2 * 3.14 * radius # circumference of a circle
print('area_of_circle:', area_of_circle) # 2826.0
print('circum_of_circle:', circum_of_circle) # 188.4

help('keywords') # list of keywords in Python 
