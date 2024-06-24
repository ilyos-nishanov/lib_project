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