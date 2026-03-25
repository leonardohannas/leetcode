"""
Chapter: String Manipulation
Problem Set: Character Manipulation

Source:
Beyond Cracking the Coding Interview

Statement (summary):
This file contains my personal solutions to the first character manipulation
questions from the String Manipulation chapter.

The exercises focus on basic ASCII-based character operations, using only
numeric character conversions such as ord() and chr().

Included questions:
- Question 1: implement a function that checks whether a character is
  alphanumeric, that is, whether it is a lowercase letter, an uppercase
  letter, or a digit between '0' and '9'.
- Question 2: implement a function that converts a lowercase character to
  uppercase. If the character is not lowercase, the function should remain
  unchanged.

Approach:
The goal of this file is to practice low-level character manipulation by
working directly with ASCII ranges instead of relying on higher-level
built-in string methods.

Concepts practiced:
- ASCII value ranges
- character classification
- lowercase and uppercase conversion
- use of ord() and chr()

Time Complexity:
Each function in this file is expected to run in O(1), since each operation
depends only on a single character.

Space Complexity:
O(1)
"""

# Question 1

def is_lowercase(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

def is_uppercase(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def is_digit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def is_alphanumeric(c):
    return is_lowercase(c) or is_uppercase(c) or is_digit(c)

# Question 2

def to_uppercase(c):
    if not is_lowercase(c):
        return 
    c = chr(ord(c) + ord('A') - ord('a'))
    return c
    

# Question 3

def split(s, c):
    splitted_strings = []
    temp_string = ""
    for char in s:
        if char == c:
            splitted_strings.append(temp_string)
            temp_string = ""
        else:
            temp_string += char
            
    splitted_strings.append(temp_string)
    return splitted_strings
            
# Question 4

def join(arr, s):
    final_string = ""
    for item in arr:
        if item == arr[-1]:
            final_string += item
        else:
            final_string += (item + s)
    
    return final_string

# Question 5: returns the first index in the string s where the string t appears in s. 
# Returns -1 if s does not contain t

def index_of(s, t):
    
    equal = True
    
    # External loop for t 
    for char_t in t:
        # Internal loop for s
        for char_s in s:
            if char_s != char_t: 
                equal = False
    
    if equal == False:
        print(f"s does not contain t")
        
                
  


if __name__ == "__main__":
    s = "abcde"
    t = "bcd"
    print(index_of(s,t))
    
