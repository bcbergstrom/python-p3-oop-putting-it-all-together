#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = None
    

    def get_shoe_size(self):
        return self._size
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    

    def set_shoe_size(self, count):
        if count is int:
            self.size = count
        else:
            print("size must be an integer")

    size = property(get_shoe_size, set_shoe_size)