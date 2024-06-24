import csv
import pprint
from datetime import date
from classtools import AttrDisplay

class Book(AttrDisplay):
    __instances = []

    def __init__(self, title, author='', isbn='', copies=1):
        self.title = title
        self.author = author    
        self.isbn = isbn
        self.copies = copies
        self.in_hands = []
    
    def add_book (book):
        Book._Book__instances.append(book)

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
    

class Patron(AttrDisplay):
    __instances = []

    def __init__(self, name, address='', id='', YOB=0):
        self.name = name
        self.address = address
        self.id = id
        self.YOB = YOB
        self.has_books=[]
        
    def add_patron(patron):
        Patron._Patron.__instances.append(patron)

    @classmethod
    def showAll(cls):
        for patron in cls.__instances:
            print(patron)
    

    
class LibraryCRUD(Book,Patron):
    
    __instances = []
    
    def borrow(patron, book):
        if book.copies > len(book.in_hands):
            book.copies -=1
            book.in_hands.append({"patron": patron.name, "time": date.today()})     #i want to add time too but how? (',').join(self, self.date)
            patron.has_books.append({"book": book.title, "time": date.today()})
            # pprint.pprint(f"{patron.name} has borrowed {book.title} at {date.today()}")
        else:
            pprint.pprint(f"Sorry, {book.title} is not available.")

    def return_book(patron, book):
        for item in patron.has_books:
            if item["book"] == book.title:
                book.copies +=1
                book.in_hands.remove({"patron": patron.name, "time": date.today()})
                patron.has_books.remove(item)
                # pprint.pprint(f"{patron.name} has returned {book.title} at {date.today()}")
                return
            pprint.pprint(f"{patron.name} does not have {book.title} to return.")

    @classmethod
    def showAll(cls):
        for instance in cls.__instances:
            print(instance)
    
            
       
def main():
    while True:
        print("\n1 View books\n2 View patrons\n3 New book\n4 New patron\n5 New borrowing\n6 Return a book\n7 LOAD OPENING BOOK INVENTORY\n0 Exit ")
        choice = input()
        if choice == '0':
            break
        elif choice == '1':
            Book.showAll()
        elif choice =='2':
            Patron.showAll()
        elif choice =='3':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book's isbn: ")
            copies = int(input("Enter number of copies: "))
            book0 = Book(title, author, isbn, copies)
            Book.add_book(book0)
            continue
        elif choice =='4':
            name = input("Enter patron's name: ")
            address = input("Enter patron's address: ")
            id = int(input('Enter id: '))    #in the future gotta make like this:  max(Patron.__instances['id'])+1
            year = int(input("Enter patron's birth year: "))
            patron0 = Patron(name, address, id, year)
            book.add_patron(patron0)
            continue
        elif choice =='5':
            patron_name = input("Enter patron's name: ")
            book_title = input("Enter book title: ")
            action0 = LibraryCRUD
            for book in Book._Book__instances:
                if book.title == book_title:
                    action0.borrow(next(p for p in Patron._Patron__instances if p.name == patron_name), book)
                    break
        elif choice =='6':
            patron_name = input("Enter patron's name: ")
            book_title = input("Enter book title: ")
            action0 = LibraryCRUD
            for book in Book._Book__instances:
                if book.title == book_title:
                    action0.return_book(next(p for p in Patron._Patron__instances if p.name == patron_name), book)
                    break
        elif choice =='7':
            file = input('show file: ')
            Book.incomming_books(file)
            

main()

