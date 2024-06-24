class Book:
    def __init__(self, nomi, autori, id, copies):
        self.title = nomi
        self.author = autori
        self.isbn = id
        self.count = copies

    def __str__(self):
        return f"{self.isbn} | Title: {self.title} | Author: {self.author}, Count: {self.count}"
    
class Patron:
    def __init__(self, patron_id, name):
        self.id = patron_id
        self.name = name
        self.borrowed_book = []
        
    def __str__(self):
        books_str = ", ".join(book.title for book in self.borrowed_book)
        return f"{self.id} | Name: {self.name} | Books: {books_str}"

class LibraryCRUD:
    def __init__(self):
        self.books = []
        self.patrons = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} added successfully!")
        
    def view_books(self):
        for i in self.books:
            print(i)
    
    def update_book(self, id, title, author, copies):
        book_to_update = [i for i in self.books if i.isbn == id][0]
        book_to_update.title  = title
        book_to_update.author  = author
        book_to_update.copies  = copies
        print(f"update successfully")
    
    def delete_book(self, id):
        self.books = [i for i in self.books if i.isbn != id]
        
        
libb = LibraryCRUD()
while True:
    print('1 add book')
    print('2 view books')
    print('3 update book')
    print('4 delete book')
    command = input()
    if command == '1':
        isbn = input('isbn: ')
        name = input('Title: ')
        author = input('author: ')
        copies = input('Copies: ')
        book = Book(name, author, isbn, copies)
        libb.add_book(book)
    elif command == '2':
        libb.view_books()
    elif command == '3':
        isbn = input('isbn: ')
        name = input('Title: ')
        author = input('author: ')
        copies = input('Copies: ')
        libb.update_book(isbn, name, author, copies)
    elif command == '4':
        isbn = input('isbn: ')
        libb.delete_book(isbn)
    else:
        break