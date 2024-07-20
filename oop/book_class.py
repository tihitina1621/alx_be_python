class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        print(f"Deleting {self.title}")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

my_book = Book("1984", "George Orwell", 1949)
print(my_book)  # Expected to use __str__
print(repr(my_book))  # Expected to use __repr__
del my_book