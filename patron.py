import csv
import datetime
from classtools import AttrDisplay

class Patron(AttrDisplay):
    __instances = []

    def __init__(self, name, address='', id='', YOB=0):
        self.name = name
        self.address = address
        self.id = id
        self.YOB = YOB
        self.has_books=[]
        self.__class__.__instances.append(self)

    @classmethod
    def incomming_patrons(cls, csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f, fieldnames=['name', 'address', 'id', 'YOB'])
            next(reader) #skip the header
            for item in reader:
                patron = cls(
                    name=item['name'],
                    address=item['address'],
                    id=item['id'],
                    YOB=int(item['YOB'])
                )
                cls.__instances.append(patron)


    @classmethod
    def showAll(cls, name=None):
        if name is None:
            for patron in cls.__instances:
                print(patron)
        else:
            for patron in cls.__instances:
                if patron.name == name:
                    print(patron)
    
    
            
            
if __name__ == '__main__':
    # Patron1 = Patron('Ali Baba', '12 JR', 46, 1900)
    # print(Patron1)
    Patron.incomming_patrons('patrons.csv')
    # Patron.showAll()
    Patron.showAll()
