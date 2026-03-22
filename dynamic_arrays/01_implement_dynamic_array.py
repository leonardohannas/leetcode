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

Approach:
Store elements in an underlying fixed-size Python list that represents the
allocated capacity. Keep track of:
- self._size: number of valid elements currently stored
- self._capacity: number of allocated slots

When the array is full and append is called, allocate a new array with double
the capacity and copy all elements over.

Time Complexity:
- append(x): amortized O(1)
- get(i): O(1)
- set(i, x): O(1)
- size(): O(1)
- pop_back(): O(1)

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
    arr = DynamicArray()

    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.append(40)
    
    arr.pop(3)
    

    print(arr)                # DynamicArray([10, 20, 30], ...)
    # print(arr.get(1))         # 20

    # arr.set(1, 99)
    # print(arr.get(1))         # 99

    # print(arr.pop_back())     # 30
    # print(arr.size())         # 2
    # print(arr)
