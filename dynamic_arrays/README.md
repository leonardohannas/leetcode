# Dynamic Arrays

This folder contains my personal solutions for the **Dynamic Arrays** chapter from *Beyond Cracking the Coding Interview*.

## Problems

- `01_dynamic_array_implementation.py` — implementation of a dynamic array from scratch, including core operations and extra methods such as indexed removal, insertion, search, and deletion by value

## Implemented methods

The current implementation includes:

- `append(x)` — adds an element to the end of the array
- `get(i)` — returns the element at index `i`
- `set(i, x)` — updates the element at index `i`
- `size()` — returns the number of stored elements
- `pop_back()` — removes and returns the last element
- `pop(i)` — removes and returns the element at index `i`
- `contains(x)` — checks whether an element exists in the array
- `insert(i, x)` — inserts an element at index `i`, shifting elements to the right
- `remove(x)` — removes the first occurrence of an element and returns its index, or `-1` if not found

## Notes

For each problem file, I keep:

- a short summary of the statement in my own words
- the Python implementation
- time and space complexity
- a structured `main()` section with valid and invalid test cases

## Goal

The goal of this folder is to document my understanding of how dynamic arrays work internally, including resizing, shifting elements, handling insertions and removals, and analyzing the complexity of each operation.