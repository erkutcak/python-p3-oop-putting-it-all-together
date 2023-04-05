#!/usr/bin/env python3
# Book in book.py gets initialized with a title. .                                                                                                                                           [  6%]
# Book in book.py has the title passed into __init__. .                                                                                                                                      [ 12%]
# Book in book.py can be assigned an author name. .                                                                                                                                          [ 18%]
# Book in book.py can be assigned a page count property. .                                                                                                                                   [ 25%]
# Book in book.py prints "page_count must be an integer" if page_count is not an integer. F                                                                                                  [ 31%]
# Book in book.py can be assigned a genre. .                                                                                                                                                 [ 37%]
# Book in book.py outputs "Flipping the page...wow, you read fast!" when method turn_page() is called F

class Book:
    def __init__(self, title, page_count=0):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if type(value) == int:
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    page_count = property(get_page_count, set_page_count)
