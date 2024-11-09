# Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.

from relationship_app.models import Book, Author, Library


def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


def query_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
