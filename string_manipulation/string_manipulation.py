"""
Chapter: String Manipulation
Problem Set: Character Manipulation

Source:
Beyond Cracking the Coding Interview

Statement (summary):
This file contains my personal solutions to the first string manipulation
questions from the String Manipulation chapter.

The exercises focus on basic ASCII-based character operations, string
splitting and joining, and substring search, using simple low-level
manipulation rather than relying on higher-level built-in methods.

Included questions:
- Question 1: implement a function that checks whether a character is
  alphanumeric, that is, whether it is a lowercase letter, an uppercase
  letter, or a digit between '0' and '9'.
- Question 2: implement a function that converts a lowercase character to
  uppercase. If the character is not lowercase, the function should remain
  unchanged.
- Question 3: implement a function that splits a string `s` into an array
  of substrings using a given character `c` as the separator.
- Question 4: implement a function that joins an array of strings into a
  single string, using a given separator string between consecutive elements.
- Question 5: implement a function `index_of(s, t)` that returns the first
  index in string `s` where string `t` appears, or `-1` if `t` does not
  occur in `s`.

Approach:
The goal of this file is to practice low-level string and character
manipulation by working directly with ASCII ranges, manual string traversal,
and explicit substring comparison instead of relying on higher-level
built-in string methods.

Concepts practiced:
- ASCII value ranges
- character classification
- lowercase and uppercase conversion
- use of ord() and chr()
- manual string splitting
- manual string joining
- substring search with direct character comparison

Time Complexity:
- Question 1: O(1)
- Question 2: O(1)
- Question 3: O(n), where n is the length of the input string
- Question 4: O(n), considering the total size of the strings being joined
- Question 5: O(nm) in the worst case, where n is the length of `s` and m is the length of `t`

Space Complexity:
- Question 1: O(1)
- Question 2: O(1)
- Question 3: O(n)
- Question 4: O(n)
- Question 5: O(1)
"""

# Question 1:

def is_lowercase(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

def is_uppercase(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def is_digit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def is_alphanumeric(c):
    return is_lowercase(c) or is_uppercase(c) or is_digit(c)

# Question 2:

def to_uppercase(c):
    if not is_lowercase(c):
        return 
    c = chr(ord(c) + ord('A') - ord('a'))
    return c
    

# Question 3:

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
            
# Question 4:

def join(arr, s):
    final_string = ""
    for item in arr:
        if item == arr[-1]:
            final_string += item
        else:
            final_string += (item + s)
    
    return final_string

# Question 5:
        
def index_of(s, t):
    lenght_t = len(t)
    lenght_s = len(s)
    for i in range(lenght_s - lenght_t + 1):
        match = True
        for j in range(lenght_t):
            if s[i+j] != t[j]:
                match = False
        if match: 
            return i
    return -1
        

if __name__ == "__main__":
    print("=== Question 1: is_alphanumeric ===")
    print("is_alphanumeric('a'):", is_alphanumeric('a'))  # True
    print("is_alphanumeric('7'):", is_alphanumeric('7'))  # True
    print("is_alphanumeric('%'):", is_alphanumeric('%'))  # False
    print()

    print("=== Question 2: to_uppercase ===")
    print("to_uppercase('b'):", to_uppercase('b'))  # B
    print("to_uppercase('G'):", to_uppercase('G'))  # None with current implementation
    print()

    print("=== Question 3: split ===")
    print("split('abc/def/ghi', '/'):", split("abc/def/ghi", '/'))
    print()

    print("=== Question 4: join ===")
    print("join(['abc', 'def', 'ghi'], '/'):", join(["abc", "def", "ghi"], '/'))
    print()

    print("=== Question 5: index_of ===")
    print("index_of('abcdefg', 'cde'):", index_of("abcdefg", "cde"))  # 2
    print("index_of('abcdefg', 'xyz'):", index_of("abcdefg", "xyz"))  # -1
    
