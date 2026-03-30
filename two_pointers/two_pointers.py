"""
Chapter: Two Pointers
Problem Set: Introductory Two-Pointer Problems

Source:
Beyond Cracking the Coding Interview

Statement (summary):
This file contains my personal solutions to introductory problems from the
Two Pointers chapter.

The goal of these exercises is to practice solving array and string problems
by using two indices that move through the data structure according to a
specific pattern.

Included questions:
- Question 1: implement a function that checks whether a string is a
  palindrome by comparing characters from both ends toward the center.

Approach:
The goal of this file is to practice the two-pointers technique, especially
the inward-pointers pattern, in which one pointer starts at the left end and
the other starts at the right end of a string or array.

Concepts practiced:
- two-pointers technique
- inward pointers
- palindrome checking
- string traversal from both ends
- constant-space comparison

Time Complexity:
- Question 1: O(n), where n is the length of the string

Space Complexity:
- Question 1: O(1)
"""

# Question 1

def palindrome(s):
    l = 0
    r = len(s) - 1
    
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
        
    return True


if __name__ == "__main__":
    s = "level"
    print(palindrome(s))
        
