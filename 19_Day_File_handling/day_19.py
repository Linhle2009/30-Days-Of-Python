### 1. File Handling:
# File handling is an import part of programming which allows us to create, read, update and delete files. 
# In Python to handle data we use open() built-in function.
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

## 1.1. Opening Files for Reading:
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

#The default mode of open is reading, so we do not have to specify 'r' or 'rt'
# Opened file has different reading methods: read(), readline, readlines. 
# An opened file has to be closed with close() method.

# read(): read the whole text as string:
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# Instead of printing all the text, let us print the first 10 characters of the text file:
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# readline(): read only the first line:
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

# readlines(): read all the text line by line and returns a list of lines:
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# After we open a file, we should close it. There is a high tendency of forgetting to close them. 
# There is a new way of opening files using with - closes the files by itself:
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


## 1.2. Opening Files for Writing and Updating:
# To write to an existing file, we must add a mode as parameter to the open() function:
# "a" - append - will append to the end of the file, if the file does not it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.

#Let us append some text to the file we have been reading:
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

# The method below creates a new file, if the file does not exist:
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

## 1.3. Deleting Files:
# We have seen in previous section, how to make and remove a directory using os module. 
# Again now, if we want to remove a file we use os module:
import os
os.remove('./files/reading_file_example.txt')

#If the file does not exist, the remove method will raise an error, so it is good to use a condition like this::
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

# --------------------- #
### 2. File Types:
## 2.1. File with txt Extension: covered in the previous section 

## 2.2. File with json Extension:
# JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# Changing JSON to Dictionary:
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


#Changing Dictionary to JSON:
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
# dumps: It stands for "dump string." Its primary job is to serialize a Python object (like your person dictionary) into a JSON formatted string
# indent=4: This is an optional but very useful argument. It controls the indentation level for pretty-printing the JSON output.
# --> If you omit indent, the JSON string will be returned as a single, compact line without any extra whitespace or newlines.


# Saving as JSON File:
# For writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f: # You opened the file in write mode ('w'), which means you can only write to it, not read from it.
    json.dump(person, f, ensure_ascii=False, indent=4)

with open('./files/json_example.json', 'r', encoding='utf-8') as f: # open the SAME file in READ mode to print its content
    file_content = f.read() # Now f is in read mode, so f.read() works!
    print(file_content)

# encoding='utf-8': This is crucial for character encoding. UTF-8 is a widely used character encoding that can represent almost all characters in the world's writing systems. 
# --> Using it ensures that special characters (like å, ä, ö which might appear in names or places) are correctly saved and can be read back without issues.

# json.dump(): This function (notice it's dump without an 's' at the end, unlike json.dumps()) is used to directly serialize a Python object and write it to a file-like object.
# f: This is the file object (opened using open()) to which the JSON data will be written.
# By default, ensure_ascii is True. When True, json.dump() (and dumps()) will escape any non-ASCII characters (e.g., å, ö, ä from Finnish names) into their \uXXXX Unicode escape sequences
# --> ensure_ascii=False: tells json.dump() to write these non-ASCII characters directly as they are, making the JSON file more readable for humans, especially if it contains international text. 
# --> This works well when coupled with encoding='utf-8'
# indent=4: Similar to json.dumps(), this argument specifies the number of spaces to use for indentation when writing the JSON data to the file. It "beautifies" the JSON


## 2.3. File with csv Extension:
# CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.
import csv
with open('./files/csv_example.csv') as f: # By default, open() opens a file in read mode ('r'), which is what we need here.
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    # delimiter=',': It tells the csv.reader what character is used to separate the values (columns) within each line of your CSV file. 
    # In this case, it's explicitly set to a comma (,), which is standard for CSV.
    line_count = 0 # initializes a variable line_count to keep track of which line number the code is currently processing. 
    # --> This is commonly used when you need to treat the header row differently from the data rows.
    for row in csv_reader: # iterates over the csv_reader iterator. In each iteration, row will be a list of strings, where each string is a value from a column in the current line of the CSV file.
        if line_count == 0: # This if block checks if it's the very first line of the file (the header row).
            print(f'Column names are :{", ".join(row)}') # . The .join() method concatenates these strings into a single string, using ", " (comma and space) as the separator between them.
            line_count += 1 # line_count += 1: Increments line_count to 1, so the next iteration will fall into the else block.
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.') 
            # This uses an f-string to format the output.
            # \t: Adds a tab indentation for visual formatting.
            # row[0]: Accesses the first element of the row list (e.g., "Asabeneh"). row[1] second element, row[2] third element    
            line_count += 1 # line_count += 1: Increments line_count for each data row processed.
    print(f'Number of lines:  {line_count}')


## 2.4. File with xlsx Extension:
# To read excel files we need to install xlrd package. We will cover this after we cover package installing using pip.:
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)


## 2.5. File with xml Extension:
# XML is another structured data format which looks like HTML. 
# In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute. 
import xml.etree.ElementTree as ET

tree = ET.parse('./files/xml_example.xml') # ET.parse(): This function is used to parse an XML file from a given file path.
# ET.parse() function returns an ElementTree object
#  This object represents the entire XML document as a tree structure, from which you can access its root element and navigate through its hierarchy.
root = tree.getroot() # retrieves the root element of the XML document. In your XML example, the <person> tag is the root element.
# --> root variable now holds an Element object (specifically, the <person> element). 
# An Element object represents an XML tag and provides attributes to access its name, attributes, and children.
print('Root tag:', root.tag) # root.tag: This attribute of an Element object returns the tag name of that element. # person
print('Attribute:', root.attrib) # root.attrib: This attribute of an Element object returns a dictionary containing all the attributes defined for that element. # {'gender': 'female'}

for child in root:  #This loop iterates directly over the root Element object. When you iterate over an Element, it yields its direct child elements one by one.
    print('field: ', child.tag)

# the xml example:
# <person gender="female">: This is the root element of this XML document.
# person is the tag name.
# gender="female" is an attribute of the person tag.
# <name>Asabeneh</name>, <country>Finland</country>, etc.: These are child elements of the person element. Each has a tag name and contains text content.
# <skills>: This is another child element of person, but it itself has nested children (<skill>).