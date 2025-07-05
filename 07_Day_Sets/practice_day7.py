# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


print(len(it_companies))  # 7
it_companies.add('Twitter')
it_companies.update(['Snapchat', 'WhatsApp'])
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'Snapchat', 'WhatsApp'}
it_companies.remove('Snapchat') # needs to be an existing item
it_companies.discard('WhatsApp') # does not raise an error if item is not found
it_companies.pop()  # removes a random item
print(it_companies)  # Remaining items after pop


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

A.union(B)  # {19, 20, 22, 24, 25, 26, 27, 28}
A.intersection(B)  # {19, 20, 22, 24, 25, 26}
A.issubset(B)  # True, A is a subset of B
A.isdisjoint(B)  # False, A and B have common elements

A.union(B)  # {19, 20, 22, 24, 25, 26, 27, 28}
print(B.union(A))  # {19, 20, 22, 24, 25, 26, 27, 28}
print(A.union(B))  # {19, 20, 22, 24, 25, 26, 27, 28}
print(B.union(A))  # {19, 20, 22, 24, 25, 26, 27, 28}

print(A.symmetric_difference(B))  # {27, 28}
print(B.symmetric_difference(A))  # {27, 28}

del A  # Deletes set A
del B  # Deletes set B 


age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(age))  # 8

age_set = set(age)  # Converts list to set, removing duplicates
print(len(age_set))  # 5, unique ages

sentence = "I am a teacher and I love to inspire and teach people"
words = set(sentence.split())  # Converts sentence to set of unique words
print(len(words))  # Number of unique words in the sentence
