# Concatenate the string
challenge = 'thirty' + ' days' + ' of' + ' python'
print(challenge)  # Output: thirty days of python

coding = 'coding' + ' for' + ' all'
print(coding)  # Output: coding for all

company = 'Coding for all'
print(company)  # Output: Coding for all
print(len(company))  # Output: 15
print(company.upper())  # Output: CODING FOR ALL
print(company.lower())  # Output: coding for all

print(company.capitalize())  # Output: Coding for all
print(company.title())  # Output: Coding For All
print(company.swapcase())  # Output: cODING FOR ALL

print(company[0:7])  # Output: Coding
print(company.find('Coding'))  # Output: 0
print(company.index('Coding'))  # Output: 0
print(company.replace('Coding', 'Python'))  # Output: Python for all
print(company.split())  # Output: ['Coding', 'for', 'all']

social_media = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(social_media.split(', '))  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(company[0])  # Output: C
print(company[last_index])  # Output: l
print(company[10])  # Output: a

#accronyms for company
acronyms = [word[0].upper() for word in company.split()]
print(''.join(acronyms))  # Output: CFALL

python = 'Python for Everyone'
acronyms_python = [word[0].upper() for word in python.split()]
print(''.join(acronyms_python))  # Output: PFE

company = 'Coding For All'
print(company.find('C'))  # Output: 0
print(company.index('C'))  # Output: 0
print(company.find('F'))  # Output: 7
print(company.rfind('l'))  # Output: 13

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))  # Output: 47 // last occurrence
print(sentence.find('because'))  # Output: 31   # first occurrence

because = sentence[sentence.find('because'):sentence.rfind('because') + len('because')]
print(because)  # Output: because because because

print(company.startswith('Coding'))  # Output: True
print(company.endswith('Coding'))  # Output: False

company = ' Coding For All '
print(company.strip())  # Output: Coding For All

company = '30 Days Of Python'
print(company.isidentifier())  # Output: False

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(', '.join(libraries))  # Output: Django, Flask, Bottle, Pyramid, Falcon



