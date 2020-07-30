from Book import Book
from Librarian import Librarian

class Members:

    members= {}  # Contains Member name as key and book he has taken from library as value

    def __init__(self,name,aadhar_id,age,location):
        self.name = name
        self.aadhar_id = aadhar_id
        self.age = age
        self.location = location
        
    # Librarian will issue a book to the member from catalog 
    def issueBook(self,librarian,catalog,book_name):
        [isbn,rack] = (librarian.remove_book_from_rack(catalog,book_name))
        Members.members[self.name]= [book_name,isbn,rack]
        Librarian.librarian_info[librarian.name] = [self.name,book_name,isbn,rack]
        print("{} has been issued {} with isbn {} at rack {} ".format(self.name,book_name,isbn,rack))
        
    # Member will return the book to Librarian who in turn adds the book to the catalog
    def returnBook(self,librarian,catalog,book_name):
        for i in catalog.book_details:
            if i[0] == book_name:
                n,a,pd,p= i[0],i[1],i[2],i[3]
                break
        for m in Members.members:
            if Members.members[m][0] == book_name:
                print("{} has returned {}".format(self.name,book_name))
                librarian.add_book_to_rack(catalog,Book(n,a,pd,p),Members.members[m][1],Members.members[m][2])
                Members.members[self.name] = "None"
                Librarian.librarian_info[librarian.name] ="None"
                break
    
    # Print all members/users taken book from the library
    def printMembers(self):
        print(Members.members)