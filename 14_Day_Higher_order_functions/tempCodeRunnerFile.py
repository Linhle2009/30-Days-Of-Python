from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Using reduce with a lambda function for summation
# lambda x, y: x + y means: take the running total (x) and add the current item (y)
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Original numbers: {numbers}")
print(f"Sum of numbers (using reduce): {sum_of_numbers}")
# Output: Sum of numbers (using reduce): 15