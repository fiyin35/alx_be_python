# Author: Fiyinfolu
# Add a Book class to initiate book title
# book author and a private attribute is_checked_out
# to track the availability of a book
# checked_out method set is_checked_out to true
# which indicate the book is available
# return_book method set is_checked_out to false
# which indicate the book is not available
# Library class manage a collection of books,
# including add_book method for adding new books to the collection,
# check_out_book method check a book out (which marks it as unavailable),
# return_book method return it (making it available again),
# and list_available_books method list all available books

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checked_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out


class Library:

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        for book in self._books:
            print(f"{book.title}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.checked_out()
                else:
                    print(f"{book} already checked out")
                return
        print(f"Available books after checking out '{title}':")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    book.return_book()
                else:
                    print(f"{book} book not checked out")
                return

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")


