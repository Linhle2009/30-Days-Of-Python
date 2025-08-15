### Python PIP - Python Package Manager ###
## 1. What is PIP ?PIP stands for Preferred installer program. We use pip to install different Python packages

## 2. Installing PIP:
# Check if pip is installed by writing: pip --version

## 3. Installing packages using pip:
# pip install numpy
import numpy ## can type this in the terminal if using "python", when finish type "exit"
numpy.version.version

# 3.1. Numpy: called numeric python. It is one of the most popular packages in machine learning and data science community.
    # a powerful N-dimensional array object
    # sophisticated (broadcasting) functions
    # tools for integrating C/C++ and Fortran code
    # useful linear algebra, Fourier transform, and random number capabilities

# 3.2. Pandas: is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. 
import pandas 

# 3.3. Web browser module: can help us to open any website. 
    # already installed by default with Python 3. 
    # if you like to open any number of websites at any time or if you like to schedule something, this webbrowser module can be used.
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

## 4. Uninstalling Packages: pip uninstall packagename

## 5. List of Packages: pip list

## 6. Show Package: pip show packagename
# If we want even more details, just add --verbose: pip show --verbose pandas

## 7. PIP Freeze: 
# Generate installed Python packages with their version and the output is suitable to use it in a requirements file. 
# A requirements.txt file is a file that should contain all the installed Python packages in a Python project.
# The pip freeze gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.

## 8. Reading from URL:
# Sometimes, we would like to read from a website using url or from an API
# API stands for Application Program Interface. It is a means to exchange structured data between servers primarily as json data. 

# 8.1. Requests - package allows to open a network connection and to implement CRUD(create, read, update and delete) operations. 
# We will see get, status_code, headers, text and json methods in requests module:
    # get(): to open a network and fetch data from url - it returns a response object
    # status_code: After we fetched data, we can check the status of the operation (success, error, etc)
    # headers: To check the header types
    # text: to extract the text from the fetched response object
    # json: to extract json data Let's read a txt file from this website

import requests # importing the request module

url = 'https://w3schools.com' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

# 8.2. Read from an API. API stands for Application Program Interface. It is a means to exchange structure data between servers primarily a json data:
import requests
url = 'https://restcountries.com/v3.1/all?fields=name,capital'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries
# --> We use json() method from response object, if the we are fetching JSON data. For txt, html, xml and other file formats we can use text.

## 9. Creating a Package:
# We organize a large number of files in different folders and sub-folders based on some criteria
# A module can contain multiple objects, such as classes, functions, etc
# A package can contain one or more relevant modules. 
# A package is actually a folder containing one or more module files

# Already done: 
    # Create a new folder named mypacakge inside 30DaysOfPython folder 
    #  Create an empty init.py file in the mypackage folder. 
    # Create modules arithmetic.py and greet.py
    # the structure should look like this:
    #─ mypackage
    # ├── __init__.py
    # ├── arithmetic.py
    # └── greet.py

# Now let's open the python interactive shell and try the package we have created:
from mypackage import arithmetics
arithmetics.add_numbers(1, 2, 3, 5)
arithmetics.subtract(5, 3)
arithmetics.multiple(5, 3)
arithmetics.division(5, 3)
arithmetics.power(5, 3)

from mypackage import greet
greet.greet_person('Asabeneh', 'Yetayeh')

# __init__.py is primarily a marker file that tells Python: "This directory is a package."
# When a package is imported, __init__.py is executed.
# An empty __init__.py simply marks the directory as a package, allowing its internal modules to be imported (e.g., from mypackage import arithmetic), 
# but it doesn't automatically expose their contents at the mypackage level.


## 10. Further Information About Packages: see the web 