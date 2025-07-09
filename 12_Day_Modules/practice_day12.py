# LEvel 1:
# Writ a function which generates a six digit/character random_user_id:
import random
import string

def random_user_id():
    chars = string.ascii_letters + string.digits # pools of characters
    user_id = ""
    for _ in range(6): #loop 6 times
        user_id += random.choice(chars)
    return user_id 
print(random_user_id());

# doesn’t take any parameters but it takes two inputs : 1 for number of characters and 1 for unber of IDs:
import random
import string
def user_id_gen_by_user():
    a = int(input("Number of characters: "))
    b = int(input("Number of IDs: "))

    chars = string.ascii_letters + string.digits # pools of characters
    for _ in range(b):
            user_id = ""
            for _ in range(a):
                user_id += random.choice(chars)
            print(user_id)
user_id_gen_by_user() # use this instead           
print(user_id_gen_by_user()) # has none in the last line becasue define doesnt have any return


# other way:
import random
import string

def user_id_gen_by_user():
    a = int(input("Number of characters: "))
    b = int(input("Number of IDs: "))

    chars = string.ascii_letters + string.digits
    
    # Create a list to hold each generated ID string
    all_ids = [] 

    for _ in range(b):
        user_id = "" # Reset for each new ID
        for _ in range(a):
            user_id += random.choice(chars)
        all_ids.append(user_id) # Add the generated ID to the list
    
    # Join all IDs in the list with a newline character between them
    # This creates a single string where each ID is on a new line
    return "\n".join(all_ids)

# Now, when you call print(user_id_gen_by_user()), it will print the single
# string that contains all IDs, each on a new line.
print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each):
import random
def rgb_color_gen():
    rgb = []
    for _ in range(3):
        color = random.randint(0, 255)
        rgb.append(color)
    return tuple(rgb)
print(rgb_color_gen())

import random
def rgb_color_gen():
    """Generates a single RGB color as a tuple (R, G, B)."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
print(rgb_color_gen())

import random
def rgb_color_gen():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_N_unique_rgb_colors(N):
    unique_colors = set()
    while len(unique_colors) < N:
        unique_colors.add(rgb_color_gen())
    return list(unique_colors) # Return as a list if you need to maintain order or list features

# Example: Generate 10 unique colors
colors = generate_N_unique_rgb_colors(10)
print(colors)
print(len(colors)) # Will always be 10 if N is <= total possible colors


## LEvel 2:
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #:
import string
import random

def list_of_hexa(): #return 1 hexa
    hexa_chars = string.hexdigits.lower()
    # Generate 6 random hexadecimal characters
    # Using a list comprehension and ''.join() is efficient for string building
    hex_code = ''.join(random.choice(hexa_chars) for _ in range(6))
    hex_color = '#' + hex_code
    return hex_color
print(list_of_hexa())

import string 
import random
def list_of_hexa(n): # return a list of hexa
    hexa_chars = string.hexdigits.lower()
    hexa = []
    for _ in range(n):
        hex_code = ''.join(random.choice(hexa_chars) for _ in range(6))
        hex_color = '#' + hex_code
        hexa.append(hex_color)
    return hexa
print(list_of_hexa(3))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array:
import string 
import random
def list_of_rgb_colors(n):
    generated_colors = []

    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # merge into 1 rgb:
        rgb_string = f"rgb({r}, {b}, {b})"
        generated_colors.append(rgb_string)
    return generated_colors
print(list_of_rgb_colors(2))

# Write a function generate_colors which can generate any number of hexa or rgb colors.
import string 
import random

def generate_colors(color, n):
    if color == 'hexa':
        hexa_chars = string.hexdigits.lower()
        hexa = []
        for _ in range(n):
            hex_code = ''.join(random.choice(hexa_chars) for _ in range(6))
            hex_color = '#' + hex_code
            hexa.append(hex_color)
        print(hexa)
    if color == 'rgb':
        rgb = []
        
        for _ in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            # merge into 1 rgb:
            rgb_string = f"rgb({r}, {b}, {b})"
            rgb.append(rgb_string)
        print(rgb)
generate_colors('hexa', 1)
generate_colors('rgb', 3)

## Level 3:
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list:
import random
def shuffle_list(lists):
    random.shuffle(lists) ### This shuffles 'input_list' directly
    return lists
mylist = ["apple", "banana", "cherry"]
print(shuffle_list(mylist))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique:
import random
def random_numbers():
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers
print(random_numbers())
