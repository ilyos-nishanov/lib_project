import unittest
from patron import Patron
from book import Book

class TestPatron(unittest.TestCase):
    def test_borrow_book(self):
        patron = Patron("John Doe")
        book = Book("Python for Beginners", 2)
        patron.borrow(book)
        self.assertTrue(book in [b["book"] for b in patron.has_books])
        self.assertTrue(patron in [b["patron"] for b in book.in_hands])

    def test_return_book(self):
        patron = Patron("Jane Doe")
        book = Book("Java for Experts", 1)
        patron.borrow(book)
        patron.return_book(book)
        self.assertFalse(book in [b["book"] for b in patron.has_books])
        self.assertFalse(patron in [b["patron"] for b in book.in_hands])

if __name__ == "__main__":
    unittest.main()