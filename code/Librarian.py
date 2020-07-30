from Catalog import Catalog

class Librarian:
    
    librarian_info = {}  # Contains Librarian as the key and details of books issued by him as values
    
    def __init__(self,name,aadhar_id,emp_id,age,location):
        self.name = name
        self.aadhar_id = aadhar_id
        self.emp_id = emp_id
        self.age = age
        self.location = location
    
    # Librarian adds a book to rack
    def add_book_to_rack(self,catalog,book,isbn,rack):
        catalog.addBookToRack(book, isbn, rack)
    
    # Librarian removes a book from the rack
    def remove_book_from_rack(self,catalog,name):
        removed = catalog.removeBookFromRack(name)
        return removed
    
    # Display all the books in the catalog
    def display_all_books(self,catalog):
        catalog.displayAllBooks()
        
    # Search a book by name
    def search_by_name(self,catalog,name):
        catalog.searchByName(name)
    
    #search a book by author name
    def search_by_author(self,catalog,author):
        catalog.searchByAuthor(author)
                
    # Print all Librarians issued book details  
    def printLibrariansIssuedBooks(self):
        print(Librarian.librarian_info) 