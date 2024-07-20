class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class EBook:
    def __init__(self, title, author, file_size):
        super().__init__(title)
        super().__init__(author)
        self.file_size = file_size
class PrintBook:
    def __init__(self, title, author, page_count)
        super().__init__(title)
        super().__init__(author)
        self.page_count = page_count
class Library:

    def add_book(self, book):
        self.book = book
    def list_books(self):
