# Level 1
age = 27

if age >= 18: 
    print("You are old enough to drive.")
else: 
    age_difference = 18 - age
    print(f"You need to wait {age_difference} more years to drive.")

my_age = 27
your_age = int(input("Enter your age: "))

if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
else:
    print("We are the same age.")


a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{b} is greater than {a}.")
else:
    print("Both numbers are equal.")

# Level 2
score = int(input("Enter your score: "))

if score >= 80 and score <= 100:
    print("You got an A.")
elif score >= 70 and score < 80:
    print("You got a B.")
elif score >= 60 and score < 70:
    print("You got a C.")
elif score >= 50 and score < 60:
    print("You got a D.")
else:
    print("You got an F.")

month = input("Enter a month: ").strip().lower()

if month in ['september', 'october', 'november']:
    print("It's autumn.")
elif month in ['december', 'january', 'february']:
    print("It's winter.")
elif month in ['march', 'april', 'may']:
    print("It's spring.")
elif month in ['june', 'july', 'august']:
    print("It's summer.")
else:
    print("Invalid month entered.")


fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()

if fruit not in fruits:
    print("That fruit is not in the list.")
    fruits.append(fruit)
    print(fruits)
else:
    print("That fruit is already in the list.")
    
# Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    middle_index = len(person['skills']) // 2
    if len(person['skills']) % 2 == 0:
        print(f"Middle skills: {person['skills'][middle_index - 1]}, {person['skills'][middle_index]}")
    else:
        print(f"Middle skill: {person['skills'][middle_index]}")
else:
    print("No skills found in the person's data.")


# check for python in skills
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python is one of the skills.")
    else:
        print("Python is not one of the skills.")
else:
    print("No skills found in the person's data.")



if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
        print("He is a front end developer.")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a backend developer.")
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")
else:
    print("No skills found in the person's data.")



if person['is_married'] == True and person['country'].lower() == 'finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")
else:
    print(f"{person['first_name']} {person['last_name']} is not married or does not live in Finland.")
