class Book:
    def __init__(self, title, author, publication_year, available_copies):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.available_copies = available_copies

    def check_availability(self):
        return self.available_copies

    def borrow_book(self, num_copies):
        if num_copies <= self.available_copies:
            self.available_copies -= num_copies
            print(f"{num_copies} copy/copies of '{self.title}' borrowed successfully.")
        else:
            print("Sorry, the requested number of copies is not available.")

    def return_book(self, num_copies):
        self.available_copies += num_copies
        print(f"{num_copies} copy/copies of '{self.title}' returned successfully.")

    def display_info(self):
        print("Book Information:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
        print("Available Copies:", self.available_copies)


# Creating an instance of Book class
book = Book("Python Crash Course", "Eric Matthes", 2015, 5)

# Displaying book information
book.display_info()

# Borrowing 3 copies of the book
book.borrow_book(3)

# Displaying updated book information
book.display_info()

book.available_copies()
# Returning 2 copies of the book
book.return_book(2)

# Displaying final book information
book.display_info()
