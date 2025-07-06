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

if person['is_married'] == True and person['country'].lower() == 'finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")
else:
    print(f"{person['first_name']} {person['last_name']} is not married or does not live in Finland.")
