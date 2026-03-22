"""
Chapter: Dynamic Arrays
Problem: Implement Dynamic Array

Source:
Beyond Cracking the Coding Interview

Statement (summary):
Implement a dynamic array data structure using a fixed-size underlying array.
Support the following operations:

- append(x): add element x to the end
- get(i): return the element at index i
- set(i, x): update the element at index i
- size(): return the number of stored elements
- pop_back(): remove and return the last element
- pop(i): remove and return the element at index i
- contains(x): return True if x is in the array, otherwise False
- insert(i, x): insert x at index i, shifting elements to the right
- remove(x): remove the first occurrence of x and return its index, or -1 if not found

Approach:
Store elements in an underlying fixed-size Python list that represents the
allocated capacity. Keep track of:
- self._size: number of valid elements currently stored
- self._capacity: number of allocated slots

When the array is full and append or insert is called, allocate a new array
with double the capacity and copy all elements over.

When the array becomes fairly empty after removals, shrink the underlying
storage to avoid wasting too much space.

Time Complexity:
- append(x): amortized O(1)
- get(i): O(1)
- set(i, x): O(1)
- size(): O(1)
- pop_back(): O(1) amortized
- pop(i): O(n)
- contains(x): O(n)
- insert(i, x): O(n)
- remove(x): O(n)

Space Complexity:
O(n)
"""


class DynamicArray:
    
    def __init__(self, initial_capacity=10):
        if initial_capacity <= 0: 
            raise ValueError("Initial capacity must be positive.")
        
        self._capacity = initial_capacity  # Number of slots in the array
        self._size = 0  # Number of elements actually stored
        self._data = [None] * self._capacity  # Initialize an empty array
        
    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds.")
        return self._data[i]
    
    def set(self, i, x):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds.")
        self._data[i] = x
        
    def size(self):
        return self._size
    
    def append(self, x):
        if self._size == self._capacity:
            self._resize()
        self._data[self._size] = x
        self._size += 1
    
    def _resize(self, new_capacity=None):
        if new_capacity is None:
            new_capacity = self._capacity * 2

        self._capacity = new_capacity
        new_data = [None] * self._capacity

        for i in range(self._size):
            new_data[i] = self._data[i]

        self._data = new_data
            
    def pop_back(self):
        if self._size == 0:
            raise IndexError("Pop from empty array.")

        popped_value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        
        # Shrink the capacity of the array if it is fairly empty
        # (e.g., only 25% full)
        if self._size / self._capacity < 0.25 and self._capacity > 10:
            self._resize(self._capacity // 2)
        
        return popped_value
    
    def pop(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds.")
    
        if i == self._size - 1:
            return self.pop_back()
        
        popped_value = self._data[i]
        
        for index in range(i, self._size - 1):
            self._data[index] = self._data[index + 1]
        
        self.pop_back()
        
        return popped_value
    
    def contains(self, x):
        for i in range(self._size):
            if self._data[i] == x:
                return True
        return False
        
    def insert(self, i, x):
        if i < 0 or i > self._size:
            raise IndexError("Index out of bounds.")
        
        if self._size == self._capacity:
            self._resize()
         
        for index in range(self._size, i, -1):
            self._data[index] = self._data[index - 1] 
        
        self._data[i] = x    
        self._size += 1
    
    def remove(self, x):
        for i in range(self._size):
            if x == self._data[i]:
                self.pop(i)
                return i   
        return -1  # Element not found
                
                  
    def __repr__(self):
        valid_items = [self._data[i] for i in range(self._size)]
        return f"DynamicArray({valid_items}, size={self._size}, capacity={self._capacity})"
        

if __name__ == "__main__":
    
    print("=== TEST 1: Create empty array ===")
    arr = DynamicArray()
    print(arr)
    print("size:", arr.size())
    print()

    print("=== TEST 2: pop_back on empty array (invalid) ===")
    try:
        arr.pop_back()
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 3: get on empty array (invalid) ===")
    try:
        arr.get(0)
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 4: set on empty array (invalid) ===")
    try:
        arr.set(0, 100)
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 5: append valid values ===")
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.append(40)
    print(arr)
    print("size:", arr.size())
    print()

    print("=== TEST 6: get valid indices ===")
    print("arr.get(0):", arr.get(0))
    print("arr.get(2):", arr.get(2))
    print()

    print("=== TEST 7: get invalid indices ===")
    try:
        arr.get(-1)
    except Exception as e:
        print("Error:", e)

    try:
        arr.get(10)
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 8: set valid index ===")
    arr.set(1, 99)
    print(arr)
    print()

    print("=== TEST 9: set invalid index ===")
    try:
        arr.set(10, 500)
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 10: contains ===")
    print("Contains 99?", arr.contains(99))
    print("Contains 123?", arr.contains(123))
    print()

    print("=== TEST 11: insert valid positions ===")
    arr.insert(0, 5)
    print("After insert(0, 5):", arr)

    arr.insert(2, 77)
    print("After insert(2, 77):", arr)

    arr.insert(arr.size(), 500)
    print("After insert(arr.size(), 500):", arr)
    print()

    print("=== TEST 12: insert invalid positions ===")
    try:
        arr.insert(-1, 111)
    except Exception as e:
        print("Error:", e)

    try:
        arr.insert(arr.size() + 1, 222)
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 13: pop valid index ===")
    removed = arr.pop(3)
    print("Removed element:", removed)
    print(arr)
    print()

    print("=== TEST 14: pop invalid indices ===")
    try:
        arr.pop(-1)
    except Exception as e:
        print("Error:", e)

    try:
        arr.pop(100)
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 15: pop_back valid ===")
    removed_last = arr.pop_back()
    print("Removed last element:", removed_last)
    print(arr)
    print()

    print("=== TEST 16: remove existing element ===")
    removed_index = arr.remove(99)
    print("Removed index:", removed_index)
    print(arr)
    print()

    print("=== TEST 17: remove non-existing element ===")
    removed_index = arr.remove(12345)
    print("Returned value:", removed_index)
    print(arr)
    print()

    print("=== TEST 18: force shrink with many pop_back operations ===")
    print("Current array before shrink test:", arr)
    while arr.size() > 0:
        print("pop_back() ->", arr.pop_back(), "|", arr)
    print()

    print("=== TEST 19: pop on empty array after clearing ===")
    try:
        arr.pop(0)
    except Exception as e:
        print("Error:", e)
    print()

    print("=== TEST 20: remove on empty array ===")
    print("Returned value:", arr.remove(10))
    print(arr)
    print()

    print("=== FINAL STATE ===")
    print(arr)
    print("size:", arr.size())