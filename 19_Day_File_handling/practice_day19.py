### Exercises: Level 1
# Write a function which count number of lines and number of words in a text:
def count_line_txt(file_txt):
    with open(f'./data/{file_txt}') as f:
        lines = len(f.readlines())
        print('Total Number of lines:', lines)


count_line_txt('obama_speech.txt')
count_line_txt('michelle_obama_speech.txt')
count_line_txt('melina_trump_speech.txt ')

def count_word_txt(file_txt):
    word = 0
    with open(f'./data/{file_txt}') as f:
        data = f.read()
        w = data.split()
        word += len(w)
        print('Total Number of words:', word)


count_word_txt('obama_speech.txt')
count_word_txt('michelle_obama_speech.txt')
count_word_txt('melina_trump_speech.txt ')


# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages:
from collections import Counter
import json

def most_spoken_language(filename, num):
    with open(f'{filename}', 'r', encoding='utf-8') as f: # open the SAME file in READ mode to print its content
        dict = json.load(f)

    language_counter = Counter()
    for country in dict:
        for lang in country["languages"]:
            language_counter[lang] += 1
 
    return ("\n".join(map(str,language_counter.most_common(num))))

print(most_spoken_language(filename='./data/countries_data.json', num=3))
print(most_spoken_language(filename='./data/countries_data.json', num=10))


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries:
import json

def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Create a list of dicts with country and population
    countries_population = [
        {'country': country['name'], 'population': country['population']}
        for country in data
    ]

    # Sort the list by population in descending order
    countries_population.sort(key=lambda x: x['population'], reverse=True)

    # Return the top n countries
    return countries_population[:n]

# Example usage
print(most_populated_countries('./data/countries_data.json', 10))

# print in each lines:
countries = most_populated_countries('./data/countries_data.json', 10)
for country in countries:
    print(country)


### Exercises: Level 2:
# Extract all incoming email addresses as a list from the email_exchange_big.txt file:
import re

def extract_emails(filename):
    with open(filename) as file:
        text = file.read()

    # Regular expression to match most email addresses
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text) #Escaped dot . (because plain dot means “any character” in regex, so \. matches a real period)

    return emails

# Example usage
emails = extract_emails('./data/email_exchanges_big.txt')
print(emails)

# Find the most common words in the English language:
import re
from collections import Counter
import os # Import os module to check for file existence

def find_most_common_word(text_or_file, n):
    text = ""
    # Check if the input is a file path
    if isinstance(text_or_file, str) and os.path.exists(text_or_file): # checks if the input is a string and if a file with that name exists
        try:
            with open(text_or_file, 'r', encoding='utf-8') as file:
                text = file.read()
        except Exception as e:
            print(f"Error reading file {text_or_file}: {e}")
            return []
    elif isinstance(text_or_file, str):
        # If it's a string and not an existing file, treat it as the text itself
        text = text_or_file

        
    words_found_by_regex = re.findall(r'\b[a-zA-Z]+\b', text, re.I) # --> Use re.findall() to extract all words
    word_counts = Counter(words_found_by_regex) # --> Count the frequencies of these words
    final_output = [(count, word) for word, count in word_counts.most_common(n)] 
    return final_output

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
print(find_most_common_word(paragraph, 3))

print(find_most_common_word('./data/obama_speech.txt', 10))
print(find_most_common_word('./data/michelle_obama_speech.txt', 10))
print(find_most_common_word('./data/donald_speech.txt', 10))
print(find_most_common_word('./data/melina_trump_speech.txt', 10))
print(find_most_common_word('./data/romeo_and_juliet.txt', 10))


## Write a python application that checks similarity between two texts: 
import re
import nltk # national language tool kit for text processing
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

## funtion to clean text:
def clean_text(text_or_file):
    text = ""
    # Check if the input is a file path
    if isinstance(text_or_file, str) and os.path.exists(text_or_file): # checks if the input is a string and if a file with that name exists
            with open(text_or_file, 'r', encoding='utf-8') as file:
                text = file.read()
    elif isinstance(text_or_file, str):
        # If it's a string and not an existing file, treat it as the text itself
        text = text_or_file

    # convert text to lower case:
    text = text.lower()

    # remove special character and digit:
    text = re.sub(r'\d+', '', text) # remove digit
    text = re.sub(r'[^\w\s]', '', text) # remove special character 

    # tokenize the text:
    tokens = nltk.word_tokenize(text)

    return tokens

# function to remove support words 
def remove_support_words(tokens):
    from data.stop_words import stop_words
    filter_tokens = [word for word in tokens if word not in stop_words]
    return  ' '.join(filter_tokens) ## need to join the words in the lists back as paragraph as tfidf takes only paragraph

# function to check similarity:
def check_text_similarity(text1_input, text2_input):
    # clean texts:
    processed_text1 = remove_support_words(clean_text(text1_input)) # clean the texts and remove stopwords
    processed_text2 = remove_support_words(clean_text(text2_input))

    # Create TF-IDF vectors
    # TfidfVectorizer expects a list of documents
    vectorizer = TfidfVectorizer()
    tfidf  = vectorizer.fit_transform([processed_text1, processed_text2]) 

    # no need to normalize, since Vectorizer will return normalized tf-idf
    similarity_matrix = tfidf * tfidf.T

    # Calculate cosine similarity
    # cosine_similarity returns a matrix, we need the [0][0] element for similarity between the two documents
    similarity_score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]

    return similarity_matrix, similarity_score

matrix_result, score_result = check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt')

print("Full Similarity Matrix:")
print(matrix_result)
print("\nSpecific Similarity Score (Text1 vs Text2):")
print(score_result)

# similarity_matrix:
 # (0, 1)        0.31048794965124715 -- 1st document to 2nd document, from 0 to 1, 31% similarity
 # (0, 0)        0.9999999999999976 -- 1st document to itself, of course identical
 # (1, 1)        0.9999999999999862 -- 2nd document to itself, same
 # (1, 0)        0.31048794965124715 -- similar to 1st one, the number is the same

# similar_score: extract from the matrix, the more direct way 


## Read the hacker news csv file and find out:
# a) Count the number of lines containing python or Python
import csv
with open('./data/hacker_news.csv', 'r', encoding='utf-8') as f: # By default, open() opens a file in read mode ('r'), which is what we need here.
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv

    # Skip the header row if your CSV has one
    next(csv_reader, None) # Skips the first row (header)

    python_line_count = 0
    for row in csv_reader:
        # Check if the row is not empty to prevent IndexError on empty lines
        if row:
            # Use 'any()' to check if 'python' (case-insensitive) is in any item (column) of the current row.
            # 'item.lower()' converts each column's content to lowercase for case-insensitive matching.
            # 'for item in row' iterates through all columns in the current row.
            if any('python' in item.lower() for item in row):
                python_line_count += 1

print(python_line_count)

# b) Count the number lines containing JavaScript, javascript or Javascript :
import csv

with open('./data/hacker_news.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  # Skip header row
    rows = 0
    for record in csv_reader: # each record is 1 line
        if any('javascript' in str(cell).lower() for cell in record): # each cell is a ob in a line
            rows += 1

print(rows)

# c) Count the number lines containing Java and not JavaScript:
import csv

count = 0
with open('./data/hacker_news.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  # Skip header

    for record in csv_reader:
        row_text = ' '.join([str(cell).lower() for cell in record])  # Combine row into one lowercase string
        if 'java' in row_text and 'javascript' not in row_text:
            count += 1

print(count)
