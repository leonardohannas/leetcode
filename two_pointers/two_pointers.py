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
- Question 5: given a string with an even number of characters, where the
  lowercase and uppercase letters appear in equal quantity, determine whether
  the word obtained from the lowercase letters matches the reverse of the
  word obtained from the uppercase letters.
- Question 6: given two arrays already sorted in nondecreasing order,
  construct and return a new sorted array containing every element from both
  inputs, preserving repeated values as many times as they occur.
- Question 7: given a sorted array of integers, determine whether there
  exists a pair of different positions whose values add up to zero, while
  using only constant extra memory.
- Question 8: given three sorted arrays, build and return a single sorted
  array containing all values from the three inputs, but keeping only one
  copy of each distinct value.

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

Question 5 uses inward-style reasoning over different character categories,
matching lowercase letters in forward order against uppercase letters in
reverse order.

Question 6 uses parallel pointers on two sorted arrays, appending the smaller
current value at each step and then adding any remaining suffix once one
array is exhausted.

Question 7 uses inward pointers on a sorted array, moving the left or right
pointer depending on whether the current sum is too small or too large.

Question 8 extends the merging idea to three sorted arrays while also
skipping repeated values in the final result.

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
- reverse matching across character groups
- merging sorted arrays
- pair-sum search in sorted arrays
- duplicate removal during merge
- constant-space comparison
- linear traversal of sorted arrays

Time Complexity:
- Question 1: O(n), where n is the length of the string
- Question 2: O(n), where n is the length of the array
- Question 3: O(n + m), where n and m are the lengths of the two arrays
- Question 4: O(n), where n is the length of the sentence
- Question 5: O(n), where n is the length of the string
- Question 6: O(n + m), where n and m are the lengths of the two arrays
- Question 7: O(n), where n is the length of the array
- Question 8: O(n + m + p), where n, m, and p are the lengths of the three arrays

Space Complexity:
- Question 1: O(1)
- Question 2: O(1)
- Question 3: O(k), where k is the size of the intersection output
- Question 4: O(1)
- Question 5: O(1)
- Question 6: O(n + m), for the merged output array
- Question 7: O(1)
- Question 8: O(n + m + p), for the merged output array in the worst case
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

def reverse_case_match(s):
    
    left_pointer, right_pointer = 0, len(s) - 1
    
    while left_pointer < right_pointer:
        
        if s[left_pointer].isupper():
            left_pointer += 1
        elif s[right_pointer].islower():
            right_pointer -= 1
        else:
            if s[left_pointer] != s[right_pointer].lower():
                return False

            left_pointer += 1
            right_pointer -= 1
    
    return True

# Question 6

def merge(arr1, arr2):
    pointer_1, pointer_2 = 0, 0
    output_arr = []
    
    while pointer_1 < len(arr1) and pointer_2 < len(arr2):
        if arr1[pointer_1] < arr2[pointer_2]:
            output_arr.append(arr1[pointer_1])
            pointer_1 += 1
        else:
            output_arr.append(arr2[pointer_2])
            pointer_2 += 1
    
    while pointer_1 < len(arr1):
        output_arr.append(arr1[pointer_1])
        pointer_1 += 1
    
    while pointer_2 < len(arr2):
        output_arr.append(arr2[pointer_2])
        pointer_2 += 1
    
    return output_arr
    
# Question 7

def two_sum_zero(arr):
    left_pointer, right_pointer = 0, len(arr) - 1
    while(left_pointer < right_pointer):
        current_sum = arr[left_pointer] + arr[right_pointer]
        if current_sum > 0:
            right_pointer -= 1
        elif current_sum < 0:
            left_pointer += 1
        else:
            return True
    return False

# Question 8

def merge_three_sorted_unique(arr1, arr2, arr3):
    pass


    


if __name__ == "__main__":
    
    # DEPOIS DE TODAS AS FUNCOES PRONTAS, ADICIONAR OS CASOS DE TESTE
    # PARA TODAS AS QUESTOES 
    
    # Test question 4
    # s = "Bob wondered, 'Now, Bob?'"
    # print(palindromic_sentence(s))
    
    # Test question 5
    # s = "haDrRAHd"
    # s = "haHrARDd"
    # print(reverse_case_match(s))
    
    # Test question 6
    # print(merge(arr1=[-1], arr2=[]))
    # print(merge(arr1=[1,3,4,5], arr2=[2,4,4]))

    # Test question 7
    # arr=[-5,-2,-1,1,1,10]
    # arr=[-3,0,0,1,2]
    # arr=[-5,-3,-1,0,2,4,6]
    # print(two_sum_zero(arr))
    
    # Test question 8
    print(merge_three_sorted_unique(arr1=[2,3,3,4,5,7], arr2=[3,3,9], arr3=[3,3,9]))
        
