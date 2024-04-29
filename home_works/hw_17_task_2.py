class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author({self.name}, {self.country}, {self.birthday})"

    def __str__(self):
        return f"Author: {self.name}, Country: {self.country}, Birthday: {self.birthday}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total_books += 1

    def __repr__(self):
        return f"Book({self.name}, {self.author}, {self.year})"

    def __str__(self):
        return f"Book: {self.name}, Author: {self.author}, Year: {self.year}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f"Library({self.name})"

    def __str__(self):
        return f"Library: {self.name}"

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


author1 = Author("John Ronald Reuel Tolkien", "United Kingdom", "January 3, 1892")
author2 = Author("Joanne Rowling", "United Kingdom", "July 31, 1965")

book1 = Book("Harry Potter and Philosopher's Stone", 1997, author2)
book2 = Book("Harry Potter and Chamber of Secrets", 1998, author2)
book3 = Book("The Hobbit", 1936, author1)

library = Library("My library")
library.books.append(book1)
library.books.append(book2)
library.books.append(book3)
library.new_book("The Lord of the Rings", 1954, author1)


print(library.books)
print(library.group_by_author(author2))
print(library.group_by_year(1954))
print(Book.total_books)
