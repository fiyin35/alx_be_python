#Author: Fiyinfolu

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
                    self._books.remove(book)
                else:
                    print(f"{book} already checked out")
                return
        print(f"Available books after checking out '{title}':")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    book.return_book()
                    self._books.append(book)
                else:
                    print(f"{book} book not checked out")
                return

    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")

