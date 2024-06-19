from datetime import datetime
from classtools import AttrDisplay
from book import Book
from patron import Patron

class LibraryCRUD(AttrDisplay):
    __instances = []

    def __init__(self, name, title, action):
        self.name = name
        self.title = title
        self.date = datetime.now()
        self.action = action
        self.__class__.__instances.append(self)

    def action(self, name, title, action):
        book = Book(title)
        patron = Patron(name)
        # Perform the desired action with the book and patron instances
        if action == 'borrow':
            book.borrow(patron)
        elif action == 'return':
            book.return_book(patron)
        else:
            raise ValueError(f'Invalid action: {action}')

        new_action = LibraryCRUD(name, title, action)
        self.__class__.__instances.append(new_action)

    @classmethod
    def show_all(cls):
        for action in cls.__instances:
            print(action)

if __name__ == '__main__':
    action1 = LibraryCRUD('Bob Smith', 'Ali Baba', 'borrow')
    action1.action('Bob Smith', 'Ali Baba', 'borrow')
    action1.show_all()