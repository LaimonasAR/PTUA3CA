from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    isbn: str


@dataclass
class Library:
    books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, isbn: str) -> bool:
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                return True
        return False

    def search_by_title(self, title: str) -> List[Book]:
        return [book for book in self.books if book.title == title]

    def search_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books if book.author == author]

    def display_books(self) -> None:
        for book in self.books:
            print(
                f"{book.title} by {book.author}, published in {book.publication_year}, ISBN: {book.isbn}"
            )


book1 = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    publication_year=1925,
    isbn="9780141392461",
)
book2 = Book(
    title="To Kill a Mockingbird",
    author="Harper Lee",
    publication_year=1960,
    isbn="9780446310789",
)

library = Library()
library.add_book(book1)
library.add_book(book2)

library.display_books()

book3 = Book(
    title="Pride and Prejudice",
    author="Jane Austen",
    publication_year=1813,
    isbn="9780486284736",
)
library.add_book(book3)

print(library.search_by_title("To Kill a Mockingbird"))
print(library.search_by_author("F. Scott Fitzgerald"))

library.remove_book("9780446310789")

library.display_books()
