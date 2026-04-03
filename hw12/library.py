"""
Library management system.

This program allows managing books and readers with basic operations:
- reserve a book
- cancel a reservation
- borrow a book
- return a book

Classes:
- Book: represents a single book and its state
- Reader: represents a library user and actions they can perform
"""


class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        if len(str(isbn)) != 13 or not str(isbn).isdigit():
            raise ValueError("ISBN must be a 13-digit number")

        if not isinstance(num_pages, int) or num_pages <= 0:
            raise ValueError("Number of pages must be a positive integer")

        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn

        self.reserved_by = None
        self.taken_by = None

    def reserve(self, reader):
        if self.reserved_by is not None:
            raise ValueError("Book is already reserved")

        if self.taken_by is not None:
            raise ValueError("Book is already taken")

        self.reserved_by = reader
        print(f"{reader.name} reserved '{self.book_name}'")

    def cancel_reserve(self, reader):
        if self.reserved_by != reader:
            raise ValueError("You cannot cancel this reservation")

        self.reserved_by = None
        print(f"{reader.name} canceled reservation of '{self.book_name}'")

    def get_book(self, reader):
        if self.taken_by is not None:
            raise ValueError("Book is already taken")

        if self.reserved_by is not None and self.reserved_by != reader:
            raise ValueError("Book reserved by another user")

        self.taken_by = reader
        self.reserved_by = None
        print(f"{reader.name} took '{self.book_name}'")

    def return_book(self, reader):
        if self.taken_by != reader:
            raise ValueError("You cannot return this book")

        self.taken_by = None
        print(f"{reader.name} returned '{self.book_name}'")


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, target_book):
        target_book.reserve(self)

    def cancel_reserve(self, target_book):
        target_book.cancel_reserve(self)

    def get_book(self, target_book):
        target_book.get_book(self)

    def return_book(self, target_book):
        target_book.return_book(self)


book = Book(
    book_name="The Hobbit", author="Books by J.R.R. Tolkien",
    num_pages=400, isbn="0006754023123"
)
vasya = Reader("Vasya")
petya = Reader("Petya")
vasya.reserve_book(book)
petya.reserve_book(book)
vasya.cancel_reserve(book)
petya.reserve_book(book)
vasya.get_book(book)
petya.get_book(book)
vasya.return_book(book)
petya.return_book(book)
