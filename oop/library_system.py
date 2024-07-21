class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        print(f'Book: {self.title} by {self.author}')
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def new2(self):
        print(f'EBook: {self.title} by {self.author}, File Size: {self.file_size}')        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def new(self):
        print(f'PrintBook: {self.title} by {self.author}, page count: {self.page_count}')

class Library:
    def add_book(self, book):
        self.books = []
        
        
        self.books.append(book)
        return book
    def list_books(self):
        for i in self.book:
            print(i)


