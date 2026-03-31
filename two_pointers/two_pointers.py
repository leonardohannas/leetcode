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
- Question 2: given an array of integers of even length, determine whether
  for every k in the range 1 <= k <= n/2, the sum of the first k elements is
  smaller than the sum of the first 2k elements.
- Question 3: given two sorted arrays of integers, return a new array with
  the elements that appear in both arrays, in sorted order, including
  duplicates present in both arrays.
- Question 4: given a sentence, determine whether its letters form a
  palindrome when differences in capitalization are ignored and non-letter
  characters such as spaces and punctuation are skipped.

Approach:
The goal of this file is to practice the two-pointers technique through
different pointer movement patterns.

Question 1 uses inward pointers, in which one pointer starts at the left end
and the other starts at the right end of a string.

Question 2 uses a slow-and-fast pointer pattern, where one pointer advances
one element at a time while the other advances two elements at a time, making
it possible to compare the sum of prefixes of size k and 2k efficiently.

Question 3 uses parallel pointers, in which one pointer moves through each
sorted array, allowing the intersection to be built efficiently by comparing
the current elements of both arrays.

Question 4 also uses inward pointers, but adds extra logic to ignore
irrelevant characters and compare letters in a case-insensitive way.

Concepts practiced:
- two-pointers technique
- inward pointers
- slow and fast pointers
- parallel pointers
- palindrome checking
- string traversal from both ends
- prefix sum comparison
- array intersection
- sentence normalization during comparison
- constant-space comparison
- linear traversal of sorted arrays

Time Complexity:
- Question 1: O(n), where n is the length of the string
- Question 2: O(n), where n is the length of the array
- Question 3: O(n + m), where n and m are the lengths of the two arrays
- Question 4: O(n), where n is the length of the sentence

Space Complexity:
- Question 1: O(1)
- Question 2: O(1)
- Question 3: O(k), where k is the size of the intersection output
- Question 4: O(1)
"""

# Question 1

def palindrome(s):
    left_pointer = 0
    right_pointer = len(s) - 1
    
    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
        
    return True

# Question 2

def smaller_prefixes(arr):
    
    slow_pointer, fast_pointer = 0, 0
    slow_sum, fast_sum = 0, 0
    
    while fast_pointer < len(arr):
        slow_sum += arr[slow_pointer]
        fast_sum += arr[fast_pointer] + arr[fast_pointer + 1]
        
        if slow_sum >= fast_sum:
            return False
        
        slow_pointer += 1
        fast_pointer += 2
        
    return True

# Question 3

def common_elements(arr1, arr2):
    pointer_1, pointer_2 = 0, 0
    output_arr = []
    while pointer_1 < len(arr1) and pointer_2 < len(arr2):
        if arr1[pointer_1] == arr2[pointer_2]:
            output_arr.append(arr1[pointer_1])
            pointer_1 += 1
            pointer_2 += 1
        else:
            if arr1[pointer_1] < arr2[pointer_2]:
                pointer_1 += 1
            else: 
                pointer_2 += 1
    return output_arr

# Question 4

def palindromic_sentence(s):
    left_pointer, right_pointer = 0, len(s) - 1
    
    while left_pointer < right_pointer:
        
        if not s[left_pointer].isalpha():
            left_pointer += 1
        elif not s[right_pointer].isalpha():
            right_pointer -= 1 
        else:
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
        
            left_pointer += 1
            right_pointer -= 1
        
    return True

# Question 5




if __name__ == "__main__":
    # Test question 4
    s = "Bob wondered, 'Now, Bob?'"
    print(palindromic_sentence(s))

        
