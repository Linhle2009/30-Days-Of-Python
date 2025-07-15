names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

# Unpack the first five countries, and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively:
*nordic_country, es, ru = names
print(nordic_country, es, ru)