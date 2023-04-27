"""You need to create a program to manage a list of books in a library. 
Each book has a title, an author, a publication year, and an ISBN. 
You need to define a Book class using the dataclass module that contains attributes for these properties. 
You also need to implement a Library class that manages a list of books. 
The Library class should allow you to add and remove books from the library, 
search for books by title or author, 
and display the list of books currently in the library."""

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from dataclasses import dataclass



@dataclass
class Books:
    title: str
    author: str
    pub_year: int
    ISBN: int


@dataclass
class Library:
    library = []

    def add_book(self, book: Books) -> None:
        self.library.append(book)
        return self.library

    def remove_book(self, title: str) -> None:
        for i, book in enumerate(self.library):
            if book.title == title:
                del self.library[i]


book_one = Books(title="Metai", author="Donelaitis", pub_year=1000, ISBN=1234)
book_two = Books(title="Whatever", author="Dunno", pub_year=1500, ISBN=1245)

print(book_one.title)
library = Library()
library.add_book(book=book_one)
library.add_book(book=book_two)
