import logging 

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


class Book:

    def __init__(self, title: str, author:str) -> str:
        self.title = title
        self.author = author

    def get_title(self):
        return f"Title: {self.title}"
    
    def get_author(self):
        return f"Author: {self.author}"
    
PP = Book("Pride and Prejudice", "Jane Austen")

H = Book("Hamlet", "William Shakespear")

WP = Book("War and peace", "Leo Tolstoy")

print(PP.get_author())

print(H.get_title())