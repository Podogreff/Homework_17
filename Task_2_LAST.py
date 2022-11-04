
class Library:
    def __init__(self, name=None, books_list=None, authors=None):
        self.name = name
        if books_list is None:
            self.books_list = []
        if authors is None:
            self.authors = []
        self.year = []

    def new_book(self, name: str, year: int, author):
        if name not in self.books_list:
            self.books_list.append(name)
        else:
            raise ValueError("This book is already added")
        if name not in self.year:
            self.year.append([name, year, author.author_name])
        else:
            raise ValueError("This book is already added")
        if author.author_name not in self.authors:
            self.authors.append(author.author_name)
        return Book

    def group_by_author(self, author):
        return f"Books by {author} author: {list(map(lambda x: x[0], filter(lambda x: x[2] == author, self.year)))}"

    def group_by_year(self, year: int):
        return f"Books by {year} year: {list(map(lambda x: x[0], filter(lambda x: x[1] == year, self.year)))}"

    @property
    def count_of_all_books(self):
        return len(self.books_list)

    def __repr__(self):
        return f"The libraty name: {self.name};\n- books: {self.books_list};\n- authors: {self.authors}"

    def __str__(self):
        return f"The libraty name: {self.name};\n- books: {self.books_list};\n- authors: {self.authors}"


class Book:
    def __init__(self, name=None, year=None, author=None):
        self.book_name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f"The Book name: {self.book_name}, year: {self.year}, author: {self.author}"

    def __str__(self):
        return f"The Book name: {self.book_name}, year: {self.year}, author: {self.author}"


class Author:
    def __init__(self, name, country, birthday, books: list):
        self.author_name = name
        self.author_country = country
        self.author_birthday = birthday
        self.authors_books = books

    def __repr__(self):
        return f"author name: {self.author_name}, country: {self.author_country}, " \
               f"birthday: {self.author_birthday}, books: {self.authors_books}"

    def __str__(self):
        return f"author name: {self.author_name}, country: {self.author_country}, " \
               f"birthday: {self.author_birthday}, books: {self.authors_books}"


#  Class Library
library1 = Library("My_library")


#  Class Author
George_Orwell = Author("George Orwell", "England", 1903, ["Animal Farm", "1984", "Coming Up for Air"])
Taras_Shevchenko = Author("Taras Shevchenko", "Ukraine", 1814, ["Katerina", "Kobzar"])
Jack_London = Author("Jack London", "England", 1903, ["Smoke Bellew", "Lost Face"])

#  Class Book
book1 = Book

#  append book to the Library
library1.new_book("1984", 1940, George_Orwell)
library1.new_book("Animal Farm", 1940, George_Orwell)
library1.new_book("Kobzar", 1840, Taras_Shevchenko)
library1.new_book("Smoke Bellew", 1942, Jack_London)

print(library1.authors)

print(library1.books_list)
print(library1)

print(library1.group_by_author("George Orwell"))
print(library1.group_by_year(1940))

print(library1.count_of_all_books)

print(George_Orwell)