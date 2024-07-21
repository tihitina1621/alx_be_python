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
    def __str__(self):
        print(f'EBook: {self.title} by {self.author}, File Size: {self.file_size}')        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def new(self):
        print(f'PrintBook: {self.title} by {self.author}, page count: {self.page_count}')
class Library:
    def __init__(self, books):
        self.books = books
    def add_book(self,book):
        self.book = book
        book = []
        book.append(self.books)
        return book
    def list_books(self):

my_library = Library()
classic_book = Book("Pride and Prejudice", "Jane Austen")
digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
my_library.add_book(classic_book)
my_library.add_book(digital_novel)
my_library.add_book(paper_novel)

my_library.list_books() 
   #library_system.py doesn't contain: ["self.books = []", "append"]
