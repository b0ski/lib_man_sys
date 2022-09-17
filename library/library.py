import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

# Open cursor to perform database operation
cur = conn.cursor()


class Book:
    genre: str
    title: str
    author: str

    def __init__(self, genre: str, title: str, author: str):
        self.title = title
        self.genre = genre
        self.author = author


class Reader:
    name: str
    gender: str
    email: str

    def __init__(self, name: str, gender: str, email: str,):
        self.name = name
        self.gender = gender
        self.email = email


class Library:
    address: str
    telephone: str
    books: list
    readers: list

    reader = None
    book = None
    has_book = {}

    def __init__(self, address: str, telephone: str, books: list, readers: list):
        self.address = address
        self.telephone = telephone
        self.books = books
        self.readers = readers

    def takeBook(self, reader, book):
        if book in self.books:
            self.books.remove(book)
            self.has_book[book] = reader
            return f'{reader.firstName} {reader.lastName} took the following book: {book.genre}, {book.title}, {book.author}'

        else:
            return 'Book is taken'

    def returnBook(self, reader, book):
        self.books.append(book)
        self.has_book[book] = None
        return f'{reader.firstName} {reader.lastName} returned the following book: {book.genre}, {book.title}, {book.author}'

    def book_log(self):
        for book in self.has_book:
            return f'{self.has_book[book].lastName} {self.has_book[book].lastName} has {book.title}'

    def write_off_book(self, book):
        self.books.remove(book)

    def add_book(self, book):
        self.books.append(book)

    def write_off_reader(self, reader):
        self.readers.remove(reader)

    def write_on_reader(self, reader):
        self.readers.append(reader)

# Close communications with database
cur.close()
conn.close()
