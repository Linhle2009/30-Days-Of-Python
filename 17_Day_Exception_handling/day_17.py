### 1. Exception Handling:
# example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device
#  If we use try and except in our program, then it will not raise errors in those blocks.

#try:
    #code in this block if things go well
#except:
    #code in this block run if things go wrong

try:
    print(10 + '5')
except:
    print('Something went wrong')

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

# In the above example, the exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except.
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

#In the code above the output is going to be TypeError. Now, let's add an additional block:
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

# try block: contains the code that might raise an error.  If an error occurs, it immediately stops executing the try block and jumps to an except block
# except blocks: are the error handlers. They run only if an error occurs in the try block.
# else block: runs only if the try block completes successfully without any errors.
# finally block: runs always, regardless of whether an error occurred in the try block or not.

#shorten the above code as follow:
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

# When you catch Exception, you are essentially saying: "Catch any error that derives from the Exception class." 
# This includes ValueError, TypeError, ZeroDivisionError, KeyError, IndexError, and many, many more common errors.
# as e: Python creates an exception object that contains details about what went wrong.

### 2. Packing and Unpacking Arguments in Python:
# 2.1. Unpacking:
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# --> it raises an error, because this function takes numbers (not a list) as arguments

#  unpack/destructure the list:
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

# We can also use unpacking in the range built-in function that expects a start and an end:
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # range(2,7) 
print(list(numbers))     # [2, 3, 4, 5, 6]

# A list or a tuple can also be unpacked like this:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# Unpacking Dictionaries:
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
## dictionary unpacking (or keyword argument unpacking) using the double asterisk (**) operator.


# 2.2 Packing:
# Sometimes we never know how many arguments need to be passed to a python function. 
# We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

# Packing Lists:
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# Packing Dictionaries:
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

# *args means "pack all remaining positional arguments into a tuple."
# **kwargs means "pack all remaining keyword arguments into a dictionary."

# In a function CALL (like your previous examples: range(*[2, 7]) or unpacking_person_info(**dct)):
# *iterable means "unpack elements from this iterable and pass them as separate positional arguments."
# **dictionary means "unpack key-value pairs from this dictionary and pass them as separate keyword arguments."


### 3. Spreading in Python:
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
## -->unpacks all its individual elements.


### 4.Enumerate: If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.
# enumerate is a tool for iteration (looping) that helps you get both the item and its index from a list or other iterable.
for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')

### 5. Zip: Sometimes we would like to combine lists when looping through them
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)


