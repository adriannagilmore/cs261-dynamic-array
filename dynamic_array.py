# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Adrianna Gilmore
import numpy as np
class DynamicArray:
    def __init__(self):
        self.capacity = 10
        self.numberOfElements = 0
        self.data = np.array([], dtype='O')
        self.next_index = 0

    def is_empty(self):
        if self.numberOfElements == 0:
            return True
        else:
            return False

    def set_numberOfElements(self, array):
        self.count = 0
        for self.i in array:
            self.count += 1
        self.numberOfElements = self.count
        return self.numberOfElements
    
    def __len__(self):
        return self.numberOfElements

    def __getitem__(self, index):
        if index < 0 or index > self.numberOfElements:
            raise IndexError('Index out of bounds')
        return self.data[index]

    def append(self, num):
        if self.numberOfElements == self.capacity:
            self.capacity *= 2
        self.newArray = np.array([num])
        self.data = np.concatenate((self.data, self.newArray))
        self.numberOfElements += 1
        self.next_index +=1

    def clear(self):
        self.data = np.array([], dtype='O')
        self.numberOfElements = 0
        self.next_index = 0

    def pop(self):
        if self.numberOfElements == 0:
            raise IndexError("Pop from empty array")
        else:
            self.newArray = self.data[self.numberOfElements-1]
            self.data = self.data[0:self.numberOfElements-2]
            self.numberOfElements -= 1
            self.next_index -= 1
            return self.newArray

    def delete(self, index):
        if self.numberOfElements == 0:
            raise IndexError("Empty Array")
        elif index <= -1 or index >= self.numberOfElements :
            raise IndexError("Index out of range")
        elif index == 0:
            self.data = self.data[1:]
            self.numberOfElements -= 1
            self.next_index -= 1 
        else:
            self.part1 = self.data[0:index]
            self.part2 = self.data[index+1:]
            self.data = np.concatenate((self.part1, self.part2)) 
            self.numberOfElements -= 1
            self.next_index -= 1       

        

    





