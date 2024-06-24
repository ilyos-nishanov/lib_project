class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

class LibraryCRUD:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Copies: {book.copies}")

    def update_book(self, isbn, title=None, author=None, copies=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if copies:
                    book.copies = copies
                break

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                break

    def add_patron(self, patron):
        self.patrons.append(patron)

    def view_patrons(self):
        for patron in self.patrons:
            print(f"Name: {patron.name}, ID: {patron.patron_id}")

    def update_patron(self, patron_id, name=None):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                if name:
                    patron.name = name
                break

    def delete_patron(self, patron_id):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                self.patrons.remove(patron)
                break

    def borrow_book(self, patron_id, isbn):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                for book in self.books:
                    if book.isbn == isbn and book.copies > 0:
                        patron.borrowed_books.append(book)
                        book.copies -= 1
                        break

    def return_book(self, patron_id, isbn):
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                for book in patron.borrowed_books:
                    if book.isbn == isbn:
                        patron.borrowed_books.remove(book)
                        for lib_book in self.books:
                            if lib_book.isbn == isbn:
                                lib_book.copies += 1
                                break
                        break

# Example usage
library = LibraryCRUD()

# Add books
book1 = Book("Book 1", "Author 1", "ISBN001", 5)
book2 = Book("Book 2", "Author 2", "ISBN002", 3)
library.add_book(book1)
library.add_book(book2)

# Add patrons
patron1 = Patron("John Doe", "P001")
patron2 = Patron("Jane Smith", "P002")
library.add_patron(patron1)
library.add_patron(patron2)

# View books and patrons
print("\nBooks in the library:")
library.view_books()
print("\nPatrons in the library:")
library.view_patrons()

# Borrow and return books
library.borrow_book("P001", "ISBN001")
library.borrow_book("P002", "ISBN002")
library.return_book("P001", "ISBN001")

# View books and patrons
print("\nBooks in the library:")
library.view_books()
print("\nPatrons in the library:")
library.view_patrons()
