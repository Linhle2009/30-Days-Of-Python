# 1. Modules: A module could be a file containing a single variable, a function or a big code base.

# 1.1 Importing a Module:
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

# 1.2. Import Functions from a Module:
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])

# 1.3. Import Functions from a Module and Renaming: 
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

# 2. Import Built-in Modules:
## 2.1 OS Module: creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.
# import the module
import os

# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')

## 2.1 Sys Module: provides functions and variables used to manipulate different parts of the Python runtime environment
# see file script.py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version


# 3. Statistics Module:provides functions for mathematical statistics of numeric data. 
from statistics import * # importing all the statistics modules:  mean, median, mode, stdev etc.
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# 4. Math Module:
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

# to check which functions the model got:
help(math)
dir(math)

#  If we want to import only a specific function from the module:
import math
from math import pi
print(pi)

# It is also possible to import multiple functions at once:
import math
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

#  import all the function in math module we can use *:
import math
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

# When we import we can also rename the name of the function:
from math import pi as  PI
print(PI) # 3.141592653589793


# 5. String Module:
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# 6. Random Module:
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

