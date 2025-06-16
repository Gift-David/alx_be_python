
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title}, {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title}, {self.author}, {self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_coount = page_count

    def __str__(self):
        return f"{self.title}, {self.author}, {self.page_coount}"

class Library:
    books = []
    def __init__(self):
        pass
    
    def add_book(self, book):

