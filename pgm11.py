# Create class Book (title, author). 
# Add attribute 'publisher' at runtime. 
# If the attribute 'publisher' is available in Book object, then print <title> written by <author> is published by <publisher>, else print 'Unknown Publisher'

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        if hasattr(self, "publisher"):
            print(f"{self.title} written by {self.author} is published by {self.publisher}")
        else:
            print("Unknown Publisher")


b1 = Book("1984", "George Orwell")
b1.publisher = "Secker & Warburg"   
b1.display()


b2 = Book("The Alchemist", "Paulo Coelho")
b2.display()
