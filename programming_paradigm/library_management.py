class Book:
    def _init_(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def get_is_checked_out(self):
        return self._is_checked_out
class Library:
    def __init__(self, _books):
        self._books = _books
    def add_book(title, author):
        global books 
        books = {}
        books.update({title: author})
        return books
    def check_out_book(title):
        books_checked_out = []
        global books
        books.pop(title)
        books_checked_out.append(title)
        return books