### Exercises: Level 1
# Count the word numbers in paragraphs:
import re
from collections import Counter
help(Counter)

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words_found_by_regex = re.findall(r'\b[a-zA-Z]+\b', paragraph, re.I)
# --> Use re.findall() to extract all words

word_counts = Counter(words_found_by_regex)
# --> Count the frequencies of these words

final_output = [(count, word) for word, count in word_counts.most_common()] 
# -->Get the most frequent word(s) in the desired format
print(final_output)


# Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20

import re
paragraph = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
regex_pattern = r'-?\d+'
# -? : Matches a hyphen zero or one time (makes the hyphen optional)

matches = re.findall(regex_pattern, paragraph)
print(matches)

matches_int = [int(num_str) for num_str in matches] # switch to interger
print(matches_int)

difference = max(matches_int) - min(matches_int)
print(difference)


### Exercises: Level 2:
# Write a pattern which identifies if a string is a valid python variable:
import re
def is_valid_variable(variable_name):
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    # Regex pattern for a valid Python variable name format
    # ^      : Start of the string
    # [a-zA-Z_]: Must start with a letter (a-z, A-Z) or an underscore (_)
    # [a-zA-Z0-9_]*: Followed by zero or more letters, digits (0-9), or underscores
    # $      : End of the string
    if re.match(regex_pattern, variable_name):  # re.match() returns a match object if the pattern matches the beginning of the string,
        return True
    else:
        return False


print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))


### Exercises: Level 3:
import re
from collections import Counter

# count three most frequent words in the string
def most_frequent_words(sentence):
    words_found_by_regex = re.findall(r'\b[a-zA-Z]+\b', sentence, re.I)
    word_counts = Counter(words_found_by_regex)
    # --> Count the frequencies of these words

    final_output = [(count, word) for word, count in word_counts.most_common(3)] 
    return final_output

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = re.sub(r'[%$@&;#!]', '', sentence)
print(cleaned_text) # The 'r' before the string creates a raw string, which is good practice for regex

print(most_frequent_words(cleaned_text))

