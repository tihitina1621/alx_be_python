class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
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