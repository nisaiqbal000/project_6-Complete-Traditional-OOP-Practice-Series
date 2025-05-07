class Book:
    total_books = 0
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Usage
b1 = Book("Book 1")
b2 = Book("Book 2")
print(Book.total_books)  # 2