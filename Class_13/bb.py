import pprint
class Library:
    my_object = {
        "book": {
            
        },
        "patron": {
            "john": {
                "name": "john"
            }
        }
    }
    
    
    def __init__(self):
        pass
    
    def add_book(self, title, author, quantity):
        Library.my_object["book"][title] = {
            "title": title,
            "author": author,
            "quantity": quantity
        }
    def add_patron(self, name: str):
        Library.my_object["patron"][name] = {
            "name": name
        }
        
    def borrow_book (self,patron, book, date, ret_date):
        if not "borrowed_books" in Library.my_object["patron"][patron]:
            Library.my_object["patron"][patron]["borrowed_books"] = []
            
        Library.my_object["patron"][patron]["borrowed_books"].append({
            "title": book,
            "date": date,
            "return_date": ret_date
        })
        Library.my_object['book'][book]['quantity'] -=1
        
    def return_book (self,patron, book, date):  
        Library.my_object['patron'][patron]['borrowed_books'] = [i for i in Library.my_object['patron'][patron]['borrowed_books'] if book != i['title']]
        Library.my_object['book'][book]['quantity'] +=1
         
    
    
    def view_object(self):
        pprint.pprint(Library.my_object)
    
    
        
        
    
library_1 = Library()
library_1.add_book("harry_potter_1", "J Rowling", 300)
library_1.add_book("harry_potter_2", "J Rowling", 400)
library_1.add_patron('william')
library_1.borrow_book("william", "harry_potter_1", '14/04/2024', '21/04/2024')
library_1.add_patron('brian')
library_1.borrow_book('brian', 'harry_potter_2', '15/03/2024', '11/04/2024')
library_1.return_book('william', 'harry_potter_1', '20/04/2024')
library_1.view_object()
