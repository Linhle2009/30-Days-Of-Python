# Python Error Types

# Go to your you computer terminal and write 'python'. The python interactive shell will be opened.

## 1. SyntaxError:
print 'hello world' # SyntaxError
# As you can see we made a syntax error because we forgot to enclose the string with parenthesis and Python already suggests the solution. Let us fix it.
print('hello world')

## 2. NameError:
print(age)
# from the message error, name age is not defined
# type of error was a NameError. We debugged the error by defining the variable name.

age = 25
print(age)

## 3. IndexError:
numbers = [1, 2, 3, 4, 5]
numbers[5]
# Python raised an IndexError, because the list has only indexes from 0 to 4 , so it was out of range.

##. 4. ModuleNotFoundError:
import maths # I added an extra s to math deliberately and ModuleNotFoundError was raised
import math # fixed by remove the s from maths

## 5. AttributeError:
import math
math.PI
# Instead of pi, I tried to call a PI function from maths module. It raised an attribute error, it means, that the function does not exist in the module. 
# It raised an attribute error, it means, that the function does not exist in the module. 

import math
math.pi

##. 5. KeyError:
users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['name']
'Asab'
users['county'] #  there was a typo in the key used to get the dictionary value. so, this is a key error and the fix is quite straight forward

users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['country']
'Finland'

## 6. TypeError:
4 + '3' # TypeError is raised because we cannot add a number to a string
# First solution would be to convert the string to int or float. 
# Another solution would be converting the number to a string (the result then would be '43')
4 + int('3') # 7
4 + float('3') # 7.0
str(4) + '3' # 43

## 7. ImportError:
from math import power # There is no function called power in the math module, it goes with a different name: pow
from math import pow
pow(2,3) #8.0

## 8. ValueError:
int('12a') # In this case we cannot change the given string to a number, because of the 'a' letter in it.

## 9. ZeroDivisionError:
1/0 # We cannot divide a number by zero.

# if you want to check more about it check the python documentation about python error types. 
# If you are good at reading the error types then you will be able to fix your bugs fast and you will also become a better programmer.
