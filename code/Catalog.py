from Book import Book

class Catalog:
    
    def __init__(self):
        self.books = { }  #contains book names as key and [isbn, rack] at which they present as values 
        self.book_details = [] # Contains list of books and details of books(name, author, publish date, pages)
        self.total_count = 0   # Contains total book count
        
    # Adds a book to the rack 
    def addBookToRack(self,book,isbn,rack):
        if self.book_details:
            for bd in self.book_details:
                if bd[0] == book.name:
                    break
            else:
                self.book_details.append([book.name,book.author,book.publish_date,book.pages])
        else:
            self.book_details.append([book.name,book.author,book.publish_date,book.pages])
        
        if book.name not in self.books:
            self.books[book.name] = list([[isbn,rack]])
            self.total_count+=1
            print("Book is added to rack")
            
        else:
            self.books[book.name].append([isbn,rack])
            self.total_count+=1
            print("Book is added to rack")

    # removes a book from rack      
    def removeBookFromRack(self,name):
        for b in self.books:
            if b == name:
                self.total_count-=1
                return self.books[name].pop()

    # Display all the books in the catalog
    def displayAllBooks(self):
        print("Total number of different books:{}".format(len(self.books)))
        print(self.book_details)
        print()
        for book in self.books:
            print("{} at {}".format(book,self.books[book]))
        print("Total Book Count:{}\n".format(self.total_count))

    # Search a book name in the catalog     
    def searchByName(self,name):
        for b in self.book_details:
            if b[0] == name:
                print(b)
                break
        else:
            print("{} is not available".format(name))
    
    # Search a book by Author name in the catalog
    def searchByAuthor(self,author):
        for a in self.book_details:
            if a[1] == author:
                print(a)
                break
        else:
            print("author name {} is not available".format(author) )