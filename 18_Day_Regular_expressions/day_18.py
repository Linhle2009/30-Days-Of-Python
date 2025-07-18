### 1. Regular Expressions:
# A regular expression or RegEx is a special text string that helps to find patterns in data
#  A RegEx can be used to check if some pattern exists in a different data type

## 1.1. The re Module & Methods in re Module:
import re

# Methods:
# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

#1.1.1 Match:
# re.match(pattern, string): Only checks if the string starts with the pattern. If the pattern is not at index 0, it returns None.

# syntac
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
# re.I (or re.IGNORECASE): Makes the matching case-insensitive. For example, if your pattern is 'hello' and re.I is used, it will match "Hello", "HELLO", "hello", etc.

import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# We can get the starting and ending position of the match as tuple using span
span = match.span() #This method returns a tuple (start_index, end_index) representing the slice of the original string where the match was found
print(span)     # (0, 15)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15

substring = txt[start:end] # You can unpack the span tuple directly into start and end variables for easier use.
print(substring)       # I love to teach

import re
txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
# --> The string does not string with I like to teach, therefore there was no match and the match method returned None.


# 1.1.2. Search:
#re.search(pattern, string): Checks if the pattern exists anywhere in the string. It returns the first re.Match object it finds, or None if the pattern isn't found at all.
# syntax
re.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag

import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first


# 1.1.3. Searching for All Matches Using findall:
# A much better re function is findall. This function checks for the pattern through the whole string and returns all the matches as a list.

import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

# -> Since we are using re.I both lowercase and uppercase letters are included. If we do not have the re.I flag, then we will have to write our pattern differently:
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']


# 1.1.4. Replacing a Substring:
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

# The following string is really hard to read unless we remove the % symbol. Replacing the % with an empty string will clean the text:
import re
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


### 2. Splitting Text Using RegEx Split:
import re
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol


### 3. Writing RegEx Patterns:
# To declare a string variable we use a single or double quote. To declare RegEx variable r''.
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# more expression see: https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md#match

## 3.1. Square Bracket:
# Let us use square bracket to include lower and upper case:
import re
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# If we want to look for the banana, we write the pattern as follows:
import re
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']


## 3.2. Escape character(\) in RegEx:
import re
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want


## 3.3. One or more times(+):
import re
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!


## 3.4. Period(.):
import re

regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
# The .+ will then consume nd banana are fruits – every character until the very end of the string (because it's greedy and . can match spaces, letters, etc., and + says "one or more")
# Since re.findall() finds non-overlapping matches, once and banana are fruits has been matched and consumed, there are no other characters left in the string for the regex to start a new match from.


## 3.5. Zero or more times(*):
# Zero or many times. The pattern could may not occur or it can occur many times.
import re

regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']


## 3.6. Zero or one time(?):
# Zero or one time. The pattern may not occur or it may occur once.
# Think of it as: Making the preceding element optional. It can be there, or it can't, but it can't be there more than once.
import re

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional; -?: Match a hyphen - zero or one time. This is the key part.
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']


## difference of * and ?:
# ? (Zero or One): The preceding element can appear 0 times or 1 time. It cannot appear more than once. It makes the element optional.
# * (Zero or More): The preceding element can appear 0 times, 1 time, 2 times, 100 times, or any number of times. It makes the element optional and repeatable.
# ex to distinguish:
import re

text = 'abbb'

# Pattern 1: 'a' followed by 'b' zero or one time
pattern_question = r'ab?'
matches_question = re.findall(pattern_question, text)
print(f"'ab?' matches in '{text}': {matches_question}")
# Output: ['ab']
# Explanation: It finds 'a', then finds 'b' (one time). It can't match 'b' again because '?' only allows zero or one.

# Pattern 2: 'a' followed by 'b' zero or more times
pattern_star = r'ab*'
matches_star = re.findall(pattern_star, text)
print(f"'ab*' matches in '{text}': {matches_star}")
# Output: ['abbb']
# Explanation: It finds 'a', then finds 'b' one or more times. Being greedy, it consumes all 'b's.


## 3.7. Quantifier in RegEx:
# We can specify the length of the substring we are looking for in a text, using a curly bracket. 
# Let us imagine, we are interested in a substring with a length of 4 characters
import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'   # 1 to 4; there cannot be a space between 1 and 4, or else there is no list
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']


## 3.8. Cart ^:
# Starts with:
import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Negation:
# When: When ^ appears as the first character inside a character set (defined by square brackets []).
# Meaning: It negates the character set. It means: "Match any single character that is NOT among the characters listed within this set."

import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
# [^A-Za-z ]: This character set means "match any single character that is NOT an uppercase letter (A-Z), NOT a lowercase letter (a-z), and NOT a space." 
# This implies it would match digits, punctuation, symbols, newlines, etc.
# +: The quantifier means "match the preceding character (which is one of these non-letters/non-spaces) one or more times."

matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
