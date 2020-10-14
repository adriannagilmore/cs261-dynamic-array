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

    def insert(self, index, object):
        self.newArray = np.array([object])
        if index <= -1 or index > self.numberOfElements:
            raise IndexError("Index out of range")
        elif index == 0:
            self.data = np.concatenate((self.newArray, self.data))
            self.numberOfElements += 1
            self.next_index += 1
        elif index == self.numberOfElements:
            self.data = np.concatenate((self.data, self.newArray))
            self.numberOfElements += 1
            self.next_index += 1
        else:
            self.part1 = self.data[0:index]
            self.part2 = self.data[index:]
            self.data = np.concatenate((self.part1, self.newArray, self.part2))
            self.numberOfElements += 1
            self.next_index += 1
    
    def is_full(self):
        if self.numberOfElements == self.capacity:
            return True
        else:  
            return False

    def max(self):
        self.max_num = 0
        if self.numberOfElements == 0:
            return None
        else:
            for element in self.data:
                if element >= self.max_num:
                    self.max_num = element
            return self.max_num
    
    def min(self):
        if self.numberOfElements == 0:
            return None
        else:
            self.min_num = self.data[0]
            for element in self.data:
                if element <= self.min_num:
                    self.min_num = element
            return self.min_num

    def sum(self):
        self.sum = 0
        if self.numberOfElements == 0:
            return None
        else:
            for element in self.data:
                self.sum += element
            return self.sum

    #could not check to see if this worked because it crashes my program
    #when I try to run it. Same with binary search.
    def linear_search(self, object):
        self.index = 0
        for element in self.data:
            self.index += 1
            if element == object:
                return self.index
            else:
                return None

    #not finished, but I think there is a better way than
    #what I am trying to do here
    #I don't how to make the splitting recusive.
    def binary_search(self, object):
        self.data = np.sort(self.data)
        self.split1 = np.array_split(self.data,2)
        self.leftSplit1 = split1[0]
        self.rightSplit1 = split1[1]
        if object < rightSplit1[0]:
            self.split2 = np.array_split(leftSplit1, 2)
        else: 
            self.split2 = np.array_split(rightSplit1,2)

        

    





