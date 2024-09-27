class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def get_is_checked_out(self):
        return self._is_checked_out
class Library:
    def __init__(self):
        #self._books = _books
        True
    def add_book(self, title, author, _book):
        self._books = []
        _book.update({title: author})
        return_book(self)
    def check_out_book(title):
        books_checked_out = []
        global books
        books.pop(title)
        books_checked_out.append(title)
        return books