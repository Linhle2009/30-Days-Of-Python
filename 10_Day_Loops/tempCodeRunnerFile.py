import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.countries_data import countries_data
print(countries_data)

# Get all unique languages from countries_data
all_languages = set()
for country in countries_data:
    for lang in country['languages']:
        all_languages.add(lang)
print("Total number of unique languages:", len(all_languages))

# 10 most spoken languages:
from collections import Counter # counts the occurrences of each element in an iterable
language_counter = Counter()
for country in countries_data:
    for lang in country['languages']:
        language_counter[lang] += 1
most_common_languages = language_counter.most_common(10)

# 10 most populated countries:
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
print("10 most populated countries:")
# lambda x: x['population'] is an anonymous function that takes a country dictionary x and returns its population.

for country in sorted_countries[:10]:
    print(f"{country['name']}: {country['population']}")
