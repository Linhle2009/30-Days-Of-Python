# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative = [i for i in numbers if i <= 0]
print(negative)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flatten = [i for row in list_of_lists for sub_row in row for i in sub_row]
print(flatten)

# Using list comprehension create the following list of tuples:
result_list_of_tuples = [
    # For each 'n' from 0 to 10 (inclusive)
    (n,) + tuple(n**power for power in range(6))
    for n in range(11) # range(11) generates numbers from 0 up to 10
]

# Print the generated list of tuples
for tpl in result_list_of_tuples:
    print(tpl)

# You can also just print the whole list:
print(result_list_of_tuples)


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
transform_countries = [
    [country.upper(), country.upper()[:3], capital.upper()] 
    for row in countries # # Outer loop: iterates through [[...]], [[...]]
    for country, capital in row  # # Inner loop: unpacks ('country', 'capital') from each sublist
]
print(transform_countries)


# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dic = [
    {'country': country.upper(), 'city': city.upper()} 
    for row in countries 
    for country, city in row
]
print(country_dic)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# Using a nested list comprehension to extract and concatenate strings
concatenated_names = [
    f"{first_name} {last_name}" # The expression to create each concatenated string
    for sublist in names       # Outer loop: iterates through [[...]], [[...]]
    for first_name, last_name in sublist # Inner loop: unpacks (first_name, last_name) from the sublist
]
print(concatenated_names)

# Write a lambda function which can solve a slope or y-intercept of linear functions.
# Lambda function to calculate the slope (m)
# It takes four arguments: x1, y1, x2, y2
calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# --- Examples ---
print("--- Slope Calculation ---")

# Example 1: Points (2, 3) and (5, 9)
# m = (9 - 3) / (5 - 2) = 6 / 3 = 2
slope1 = calculate_slope(2, 3, 5, 9)
print(f"Slope for (2,3) and (5,9): {slope1}") # Output: 2.0

# Example 2: Points (1, 5) and (4, -1)
# m = (-1 - 5) / (4 - 1) = -6 / 3 = -2
slope2 = calculate_slope(1, 5, 4, -1)
print(f"Slope for (1,5) and (4,-1): {slope2}") # Output: -2.0

# Example 3: Horizontal line (slope = 0)
# m = (7 - 7) / (10 - 0) = 0 / 10 = 0
slope3 = calculate_slope(0, 7, 10, 7)
print(f"Slope for (0,7) and (10,7): {slope3}") # Output: 0.0

# Example 4: Vertical line (slope is undefined, will cause ZeroDivisionError)
# Uncomment the line below to see the error
# slope_undefined = calculate_slope(3, 1, 3, 5)
# print(f"Slope for (3,1) and (3,5): {slope_undefined}")

# Lambda function to calculate the y-intercept (b)
# It takes three arguments: x (from a point), y (from a point), and m (the slope)
calculate_y_intercept = lambda x, y, m: y - m * x # y=mx+b

# --- Examples ---
print("\n--- Y-intercept Calculation ---")

# Example 1: Line with slope m=2 passing through (5, 9)
# b = 9 - 2 * 5 = 9 - 10 = -1
y_intercept1 = calculate_y_intercept(5, 9, 2)
print(f"Y-intercept for point (5,9) and slope 2: {y_intercept1}") # Output: -1

# Example 2: Line with slope m=-2 passing through (1, 5)
# b = 5 - (-2) * 1 = 5 + 2 = 7
y_intercept2 = calculate_y_intercept(1, 5, -2)
print(f"Y-intercept for point (1,5) and slope -2: {y_intercept2}") # Output: 7

# Example 3: Line with slope m=0.5 passing through (4, 7)
# b = 7 - 0.5 * 4 = 7 - 2 = 5
y_intercept3 = calculate_y_intercept(4, 7, 0.5)
print(f"Y-intercept for point (4,7) and slope 0.5: {y_intercept3}") # Output: 5.0