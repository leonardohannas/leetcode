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
- Question 9: given an array that first goes down and then goes up, return
  a new array with the same elements arranged in sorted order, taking into
  account that repeated values may appear.
- Question 10: given a sorted array of integers and a closed interval
  [low, high], return all numbers inside that interval that do not appear
  in the array.
- Question 11: given two sorted lists of disjoint closed intervals, return
  the intervals that belong to both lists, keeping the result sorted and
  merging any consecutive overlap into a single interval when needed.

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

Question 9 relies on the fact that the array can be viewed as two sorted
parts: a nonincreasing prefix and a nondecreasing suffix. The problem can
then be solved by merging those two parts.

Question 10 uses a parallel-pointers idea between the sorted input array and
the implicit sorted sequence low, low + 1, ..., high, without needing to
materialize that second sequence.

Question 11 uses parallel pointers over two interval lists. At each step, it
either skips the interval that ends earlier or adds the overlap between the
current pair when they intersect.

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
- sorting a valley-shaped array by merging two ordered parts
- finding missing values in a numeric range
- interval intersection
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
- Question 9: O(n), where n is the length of the array
- Question 10: O(n + r), where n is the length of the array and
  r = high - low + 1
- Question 11: O(n + m), where n and m are the numbers of intervals in the
  two input arrays

Space Complexity:
- Question 1: O(1)
- Question 2: O(1)
- Question 3: O(k), where k is the size of the intersection output
- Question 4: O(1)
- Question 5: O(1)
- Question 6: O(n + m), for the merged output array
- Question 7: O(1)
- Question 8: O(n + m + p), for the merged output array in the worst case
- Question 9: O(n), for the output array
- Question 10: O(k), where k is the number of missing values returned
- Question 11: O(k), where k is the number of intersection intervals returned
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
    while left_pointer < right_pointer:
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
    
    pointer_1, pointer_2, pointer_3 = 0, 0, 0
    output_arr = []
    
    while pointer_1 < len(arr1) or pointer_2 < len(arr2) or pointer_3 < len(arr3):
        
        candidates = []
        
        if pointer_1 < len(arr1):
            candidates.append(arr1[pointer_1])
        if pointer_2 < len(arr2):
            candidates.append(arr2[pointer_2])
        if pointer_3 < len(arr3):
            candidates.append(arr3[pointer_3])
            
        current_min = min(candidates)
        
        if not output_arr or output_arr[-1] != current_min:
            output_arr.append(current_min)
        
        while pointer_1 < len(arr1) and arr1[pointer_1] == current_min:
            pointer_1 += 1
            
        while pointer_2 < len(arr2) and arr2[pointer_2] == current_min:
            pointer_2 += 1
            
        while pointer_3 < len(arr3) and arr3[pointer_3] == current_min:
            pointer_3 += 1
            
    return output_arr
            
# Question 9

def sort_valley_array(arr):

    pointer = 0
    index_min_element = 0
    min_element = arr[0]
    while pointer < len(arr):
        if arr[pointer] < min_element:
            min_element = arr[pointer]
            index_min_element = pointer
        pointer += 1  
    
    new_arr = []
    left_pointer = index_min_element
    right_pointer = index_min_element - 1
    
    while right_pointer >= 0 and left_pointer < len(arr):
        
        if arr[left_pointer] < arr[right_pointer]:
            new_arr.append(arr[left_pointer])
            left_pointer += 1
        else:
            new_arr.append(arr[right_pointer])
            right_pointer -= 1
            
    while right_pointer >= 0:
        new_arr.append(arr[right_pointer])
        right_pointer -= 1
        
    while left_pointer < len(arr):
        new_arr.append(arr[left_pointer])
        left_pointer += 1
        
    return new_arr
        
# Question 10

def missing_numbers_in_range(arr, low, high):
    output_arr = []
    i = 0
    for value in range(low, high + 1):
        while i < len(arr) and arr[i] < value:
            i += 1
        
        if i == len(arr) or arr[i] != value:
            output_arr.append(value)
            
    return output_arr

# Question 11

# Returns the overlap between two intervals of the form [start, end].
# This function assumes the intervals already overlap.
def intersection(interval_1: list[int], interval_2: list[int]) -> list[int]:
    start_interval_1, end_interval_1 = interval_1
    start_interval_2, end_interval_2 = interval_2

    overlap_start = max(start_interval_1, start_interval_2)
    overlap_end = min(end_interval_1, end_interval_2)

    return [overlap_start, overlap_end]


# Returns the intersection between two sorted lists of non-overlapping intervals.
# Each interval is represented as [start, end], with both endpoints included.
def intervals_intersection(arr1: list[list[int]], arr2: list[list[int]]) -> list[list[int]]:
    result = []

    number_intervals_arr1 = len(arr1)
    number_intervals_arr2 = len(arr2)

    pointer_arr1 = 0
    pointer_arr2 = 0

    while pointer_arr1 < number_intervals_arr1 and pointer_arr2 < number_intervals_arr2:
        current_interval_arr1 = arr1[pointer_arr1]
        current_interval_arr2 = arr2[pointer_arr2]

        start_current_interval_arr1, end_current_interval_arr1 = current_interval_arr1
        start_current_interval_arr2, end_current_interval_arr2 = current_interval_arr2

        # If arr1's current interval ends before arr2's current interval starts,
        # there is no overlap and we can advance pointer_arr1.
        if end_current_interval_arr1 < start_current_interval_arr2:
            pointer_arr1 += 1

        # If arr2's current interval ends before arr1's current interval starts,
        # there is no overlap and we can advance pointer_arr2.
        elif end_current_interval_arr2 < start_current_interval_arr1:
            pointer_arr2 += 1

        # Otherwise, the intervals overlap. We add the overlap to the result
        # and advance the pointer of the interval that ends first.
        else:
            result.append(intersection(current_interval_arr1, current_interval_arr2))

            if end_current_interval_arr1 < end_current_interval_arr2:
                pointer_arr1 += 1
            else:
                pointer_arr2 += 1

    return result

# Question 12




            
    


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
    # print(merge_three_sorted_unique(arr1=[2,3,3,4,5,7], arr2=[3,3,9], arr3=[3,3,9]))
    
    # Test question 9
    # arr = [8,4,2,2,1,6]
    # arr = [1,2]
    # arr = [2,2,1,1]
    # print(sort_valley_array(arr))
    
    # Test question 10
    #
    # arr = [6,9,12,15,18]
    # low = 9
    # high = 13
    #
    # arr = [6,9,12,15,18]
    # low = 1
    # high = 100
    #
    # arr = [6,7,8,8]
    # low = 9
    # high = 9
    #
    # arr = [6,7,8,8]
    # low = 7
    # high = 8
    # print(missing_numbers_in_range(arr, low, high))
    
    # Test question 11
    # arr1 = [[0,1], [4,6], [7,8]] 
    # arr2 = [[2,3], [5,9], [10,11]]
    # print(intervals_intersection(arr1, arr2))

    # Test question 12
    arr1 = [[0,1], [4,6], [7,8]] 
    arr2 = [[2,3], [5,9], [10,11]]
    print(intervals_intersection(arr1, arr2))
    pass
        
