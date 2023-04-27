"""Create a class to represent a library system. 
The library system should have a collection of books that can be borrowed by users. 
Users can register to the library system, borrow books, and return books. 
The library system should keep track of the books borrowed by users, 
and the number of available copies of each book."""


class Library:
    def __init__(self) -> None:
        pass

    # def register(self):
    #     pass

    def borrow(self):
        pass

    def return_book(self):
        pass


class Book:
    def __init__(
        self,
        author: str,
        title: str,
    ) -> None:
        self.author = author
        self.title = title


class Books:
    books = []

    @classmethod
    def register_book(cls, book: Book):
        cls.books.append(book)


class Reader:
    def __init__(self, full_name: str, books_borrowed: int) -> None:
        self.full_name = full_name
        self.books_borrowed = books_borrowed


class Readers:
    readers = []

    @classmethod
    def register_reader(cls, reader: Reader):
        cls.readers.append(reader)

    # classmethod to return data from class
    @classmethod
    def list_readers(cls):
        return cls.readers


book1 = Book("Charles Dickens", "A Tale of Two Cities")
book2 = Book("Antoine de Saint-Exupéry", "The Little Prince")
book3 = Book("J. K. Rowling", "Harry Potter and the Philosopher's Stone")

reader_one = Reader("Laimonas Paura", 0)
reader_two = Reader("Dwayne Johnson", 0)
reader_three = Reader("Dan Brown", 0)

Books.register_book(book1)
Books.register_book(book2)
Books.register_book(book3)

Readers.register_reader(reader_one)
Readers.register_reader(reader_two)
Readers.register_reader(reader_three)


print(reader_two.full_name)
print(Readers.readers)
print(Books.books)

readers_list = Readers.list_readers() #return value from class values

for reader in readers_list:
    print(reader.full_name)
