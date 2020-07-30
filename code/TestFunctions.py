from Book import Book
from Catalog import Catalog
from Librarian import Librarian
from Member import Members

b1 = Book('Shoe Dog','Phil Knight', '2015',312)
b2 = Book('Moonwalking with Einstien','J Foer', '2017',318)

c = Catalog()
c.addBookToRack(b1, '123hg','H1B2')
c.addBookToRack(b1, '124hg','H1B4')
c.addBookToRack(b1, '125hg','H1B5')
c.addBookToRack(b1, '126hg','H1B6')

c.addBookToRack(b2, '463hg','K1B2')
c.addBookToRack(b2, '464hg','K1B4')
c.addBookToRack(b2, '465hg','K1B5')
c.addBookToRack(b2, '466hg','K1B6')

c.displayAllBooks()

c.searchByName("Shoe Dog")

c.searchByAuthor("J Foer")

c.removeBookFromRack("Moonwalking with Einstien") # remove a book from rack

c.displayAllBooks()

l1= Librarian("Awantik",'asljlkj22','zeke101',34,"Bangalore") 
l2 = Librarian('Rakesh',"apljkj23","zeke102",35,"Bangalore")

l1.add_book_to_rack(c,b2,'466hg','K1B6') # Librarian l1 adds a book to rack

c.displayAllBooks()

m1= Members("Vish","asl23",23,"Bangalore")
m2 = Members("Ram","pq123",30,"Bangalore")

m1.issueBook(l1,c,"Shoe Dog") # Member m1 is issued a "Shoe Dog" book from catalog c by librarian l1

c.displayAllBooks()

m2.issueBook(l2,c,"Moonwalking with Einstien") # Member m2 is issued a "Moonwalking with Einstien" book from catalog c by librarian l2

c.displayAllBooks()

l1.printLibrariansIssuedBooks()

m1.printMembers()

m1.returnBook(l1,c,"Shoe Dog") #Member m1 returned "Shoe Dog" book to librarian l1 and catalog c
 
c.displayAllBooks()

m2.returnBook(l2,c,"Moonwalking with Einstien") # Member m2 returned "Moonwalking with Einstien" book to librarian l2 and catalog c

c.displayAllBooks()





