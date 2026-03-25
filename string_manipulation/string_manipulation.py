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