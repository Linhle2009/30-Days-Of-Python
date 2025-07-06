dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {   'name': 'Buddy',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 5
    }

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe', 
    'is_female': True,
    'age': 20,
    'marital_status': 'single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': {
        'street': '123 Main St',
        'zipcode': '10001'
    }
}   
print(len(student))  # Print the length of the student dictionary

# Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)  # ['Python', 'JavaScript']
print(type(skills))  # <class 'list'>

# Modify the skills values by adding one or two skills
student['skills'].extend(['HTML', 'CSS'])
print(student['skills'])  # ['Python', 'JavaScript', 'HTML', 'CSS']

# Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)  # ['first_name', 'last_name',     

# Get the dictionary values as a list
value_list = list(student.values())
print(value_list)  # ['John', 'Doe', True, 20, 'single', ['Python', 'JavaScript', 'HTML', 'CSS'], 'USA', 'New York', {'street': '123 Main St', 'zipcode': '10001'}]

# change the dictionary to a list of tuples
items_list = list(student.items())
print(items_list)  # [('first_name', 'John'), ('last_name', 'Doe'),

# delete one of the items in the dictionary
del student['address']
print(student)  # {'first_name': 'John', 'last_name': 'Doe',

del student # This will delete the entire student dictionary
