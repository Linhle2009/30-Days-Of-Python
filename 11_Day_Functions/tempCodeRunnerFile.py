
import sys
import os
from collections import Counter # counts the occurrences of each element in an iterable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data
print(countries_data)

def most_spoken_language(dict):
    language_counter = Counter()
    for country in dict:
        for lang in country['languages']:
            language_counter[lang] += 1
    return language_counter.most_common(10)
print(most_spoken_language(countries_data))

def most_populated_countries(dict):
    sorted_countries = sorted(dict, key=lambda x: x['population'], reverse=True)
    return sorted_countries
print(most_populated_countries(countries_data))

