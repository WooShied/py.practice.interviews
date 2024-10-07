# Create a simple library management system where users
# can check some details on the book and see if they can rent
# it if that book is available and hasn't been borrowed already.
# To get information for a book, user should be able to look up
# book by any of the Book's properties, except publish date.
# Once rented, user should be allowed to return the book.

# A book would have the following details:
# Title
# Author
# publish date (mm/dd/yy)
# serial number

# Add the following books in the system

# Title: Oliver Twist
# Author: Charles Dickens
# Publish date: 12/04/98
# Serial number: 1298420

# Title: To Kill a Mockingbird
# Author: Harper Lee
# Publish date: 07/11/60
# Serial number: 6543210

# Title: The Great Gatsby
# Author: F. Scott Fitzgerald
# Publish date: 04/10/25
# Serial number: 9876543

# Title: 1984
# Author: George Orwell
# Publish date: 06/08/49
# Serial number: 1122334

# Title: Moby Dick
# Author: Herman Melville
# Publish date: 11/14/51
# Serial number: 9988776

# What about availablility? how and where would you track that?

# To insert in dict: my_dict[my_key] = my_value

# This part is good so far <3
class Books:
    def __init__(self, title, author, publish_date, serial_number: str):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.serial_number = serial_number
        self.checked_out = False

    def book_status(self):
        status = "checked out" if self.checked_out else "Is Avalable" # <- yea, no peeking anywhere hows line 67
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"publish date:{self.publish_date}")
        print(f"Serial Number {self.serial_number}")


class Managment:
    def __init__(self):
        self.books = []

    def input_books(self, title, author, publish_date, serial_number: str):
        add_book = Books(title, author, publish_date, serial_number)
        # self.books[serial_number] = add_book
        self.book.append(add_book)
        print(f"Added {title}, Serial number: {serial_number}")
    
    def check_out(self, anything_related_to_the_book: str):
        for book in self.books:
            if anything_related_to_the_book == book.title or anything_related_to_the_book == book.author or anything_related_to_the_book == book.serial_number:
                book.checked_out = True
        # if serial_number in self.books:
        #     Books = self.books[serial_number]
        #     if not Books.checked_out:
        #         Books.checked_out = True
        #         print(f"checked out {Books.title}")
        #     else:
        #         print(f"The book {Books.title} is already checked out")
        # else:
        #     print(f"Serial number {serial_number} was not found")

    def check_in(self, serial_number: str):
        if serial_number in self.books:
            Books = self.books[serial_number]
            if Books.checked_out:
                Books.checked_out = False
                print(f"checked in book {Books.title}")
            else:
                print(f"Book already checked in {Books.title}")
        else:
            print(f"Serial number {serial_number} was not found")

    def look_up(self, anything: str):
        for serial_number, book in self.books.items():
            print(f"Checking book {book.title}")
            if anything == book.title or anything == book.author or anything == book.serial_number:
                print(f"Here is the book you are looking for {book.title} {book.author} {book.serial_number}")
                return

        print(f"that book does not exist {anything}")


Mission_viejo_library = Managment()
Mission_viejo_library.input_books("Oliver Twist", "Charles Dickens", "12/04/98", "1298420")
Mission_viejo_library.input_books("To Kill a Mockingbird", "Harper Lee", "07/11/60", "6543210")
Mission_viejo_library.input_books("TEST BOOK 1", "Harper Lee", "07/11/60", "1234")
Mission_viejo_library.input_books("TEST BOOK 1", "Harper Lee", "07/11/60", "12345")
Mission_viejo_library.input_books("TEST BOOK 1", "Harper Lee", "07/11/60", "123456")
Mission_viejo_library.check_out("1298420")
Mission_viejo_library.check_out("1298420")
Mission_viejo_library.look_up("Charlebto")
