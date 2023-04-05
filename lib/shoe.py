#!/usr/bin/env python3
# FAILED Shoe in shoe.py gets initialized with a brand. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py has the brand passed to __init__. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a color. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a size. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py prints "size must be an integer" if size is not an integer. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a material. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a condition. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py says that the shoe has been repaired. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py has "New" condition after repair. - TypeError: Shoe() takes no arguments
class Shoe:
    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = 0
    
    def cobble(self):
        self.condition = "New"
        print('Your shoe is as good as new!')
    
    def get_size(self):
        return self._size
    
    def set_size(self, value):
        if type(value) == int:
            self._size = value
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)