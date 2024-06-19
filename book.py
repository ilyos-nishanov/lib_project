import csv
from classtools import AttrDisplay

class Book(AttrDisplay):
    __instances = []

    def __init__(self, title, author='', isbn='', copies=1):
        self.title = title
        self.author = author    
        self.isbn = isbn
        self.copies = copies
        self.__class__.__instances.append(self)

    @classmethod
    def incomming_books(cls, csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f, fieldnames=['title', 'author', 'isbn', 'copies'])
            next(reader) #skip the header
            for item in reader:
                book = cls(
                    title=item['title'],
                    author=item['author'],
                    isbn=item['isbn'],
                    copies=int(item['copies'])
                )
                cls.__instances.append(book)

    @classmethod
    def showAll(cls):
        for book in cls.__instances:
            print(book)
    
    # def lend(self, title, patron_id, period)        
    
            
            
if __name__ == '__main__':
    book1 = Book('Bob Smith', 'JR', 1, 100)
    # print(book1)
    Book.incomming_books('books.csv')
    Book.showAll()
