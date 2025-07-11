### 1. Higher Order Functions
#A function can take one or more functions as parameters
#A function can be returned as a result of another function
#A function can be modified
#A function can be assigned to a variable

## 1.1 Function as a Parameter:
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter, here f is the sum_numbers function that we just defined
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5]) 
print(result)       # 15

## 1.2. Function as a Return Value:
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
## --> You can see from the above example that the higher order function is returning different functions depending on the passed parameter


### 2. Python Closures:
# closure is created by nesting a function inside another encapsulating function and then returning the inner function
# A closure is a function object that remembers values from its enclosing lexical scope (even if that scope no longer exists physically).

def add_ten():
    ten = 10 # Enclosing Scope: The scope of add_ten is where ten lives.
    def add(num): # Function: add is the function.
        return num + ten # Remembered Value: add "remembers" that ten was 10 at the time add_ten was called and add was returned.
    return add # add_ten() returns the 'add' function itself

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

### 3. Python Decorators:
#  allows a user to add new functionality to an existing object without modifying its structure. 
# --> A decorator is a function that takes another function, 
# adds some capability to it, and then gives you back a new (modified) version of that function, 
# without you ever having to touch the original function's code.


#3.1 To create a decorator function, we need an outer function with an inner wrapper function.
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON -- g() means: "Execute the function that g refers to."

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function): # This is the 'wrapper' function
    def wrapper(): # This is the 'inner wrapper' that does the work
        func = function()  # 1. Call the original function (the 'gift')
        make_uppercase = func.upper() # 2. Add the new functionality (the 'flair')
        return make_uppercase # 3. Return the result with flair
    return wrapper # The decorator returns the 'inner wrapper' function itself
@uppercase_decorator # shortcut) for the manual way above. 
# Take the greeting function definition that comes right after me, pass it to uppercase_decorator, and whatever uppercase_decorator returns, reassign that back to the name greeting."
# greeting = uppercase_decorator(greeting) # This happens automatically!
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON you are no longer calling the original greeting function. 
# --> You are calling the wrapper function that uppercase_decorator returned, which now has the responsibility of calling the original function and uppercasing its output.


# 3.2 Applying Multiple Decorators to a Single Function:

'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator # Python applies them from bottom to top (or closest to the function definition first, then moving upwards)
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   ['WELCOME', 'TO', 'PYTHON']


# 3.3 Accepting Parameters in Decorator Functions:
# Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.
def decorator_with_parameters(function): # 'function' here is the original 'print_full_name'
    ## This 'wrapper_accepting_parameters' WILL BE the new 'print_full_name'
    def wrapper_accepting_parameters(para1, para2, para3): # It must accept arguments
        # 1. First, the decorator calls the original function
        function(para1, para2, para3) 
        # 2. Then, the decorator adds its own new functionality
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters # The decorator returns this new 'wrapper' function

@decorator_with_parameters
def print_full_name(first_name, last_name, country): # This is the original function
    print("I am {} {}. I love to teach.".format(first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland') # Calling the decorated function

## --> explain:
# The Core Idea: The Wrapper Must Match the Original Function's Signature
# after decorator: print_full_name = decorator_with_parameters(print_full_name)
# This means the variable print_full_name (after decoration) will now point to the wrapper_accepting_parameters function that the decorator returns.
# Therefore, for this to work, the wrapper_accepting_parameters function must be able to accept the same arguments that print_full_name is expected to receive (first_name, last_name, country).

# Common Practice (*args, **kwargs):
# you'll often see *args and **kwargs used in the wrapper function to make it flexible enough to accept any number of positional and keyword arguments, 
# rather than hardcoding para1, para2, para3:
def decorator_with_any_parameters(function):
    def wrapper_any_parameters(*args, **kwargs): # Accepts any arguments
        result = function(*args, **kwargs)       # Passes all arguments to original
        print(f"Function {function.__name__} was called with args: {args}, kwargs: {kwargs}")
        return result
    return wrapper_any_parameters

@decorator_with_any_parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

@decorator_with_any_parameters
def add(a, b):
    return a + b

print(greet("Alice"))       # Output: Function greet was called with args: ('Alice',), kwargs: {}
print(add(5, b=10))         # Output: Function add was called with args: (5,), kwargs: {'b': 10}


### 4. Built-in Higher Order Functions
# they take another function as an argument.
# Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. 
# Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

# 4.1 Python - Map Function:
# The map() function is a built-in function that takes a function and iterable as parameters.
# It's a concise alternative to a for loop when you want to create a new list where each element is the result of some operation on the corresponding element of an existing list.
# syntax
map(function, iterable)

#Example:1
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

#Example:2
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

#Example:3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


# 4.2 Python - Filter Function:
# The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). 
# It filters the items that satisfy the filtering criteria.
    # syntax
filter(function, iterable)

# Example:1
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

#Example:2
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original numbers: {numbers}")
print(f"Even numbers (using filter): {even_numbers}")
# Output: Even numbers (using filter): [2, 4, 6, 8, 10]

# Equivalent using a for loop:
# even_numbers_loop = []
# for x in numbers:
#     if x % 2 == 0:
#         even_numbers_loop.append(x)


# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']

#4.3 Python - Reduce Function: 
# To apply a function cumulatively to the items of a sequence, reducing the sequence to a single value. 
# It's used for aggregations, like summing all numbers, finding the product, or finding the maximum.

# Example:1
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15


from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Using reduce with a lambda function for summation
# lambda x, y: x + y means: take the running total (x) and add the current item (y)
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Original numbers: {numbers}")
print(f"Sum of numbers (using reduce): {sum_of_numbers}")
# Output: Sum of numbers (using reduce): 15

# Equivalent using a for loop:
# total = 0
# for x in numbers:
#     total += x

#### difference btw map and reduce
# map: Transformation (One-to-One, or Each Item Individually)
    # Purpose: To transform each individual item in an iterable according to a given function.
    # Output: It returns a new iterable (like a list or tuple) where each element is the result of applying the function to the corresponding element of the original iterable
# reduce: Aggregation / Reduction (Many-to-One)
    # Purpose: To reduce an iterable down to a single cumulative value by repeatedly applying a function to pairs of elements.
    # Output: It returns a single value (not an iterable).
    # How it works: It takes the first two elements, applies the function, then takes that result and the next element, applies the function again, and so on, until only one value remains.