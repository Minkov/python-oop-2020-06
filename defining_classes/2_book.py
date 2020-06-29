from dataclasses import dataclass


class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

@dataclass
class Book:
    name: str
    author: str
    pages: int





book = Book2("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
print(book)
