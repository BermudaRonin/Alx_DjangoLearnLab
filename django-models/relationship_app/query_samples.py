from .models import Book, Library

# Query all books by a specific author.

def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

# List all books in a library.

def get_books_in_library(library_name):
    books = Book.objects.filter(library__name=library_name)
    return books

# Retrieve the librarian for a library.

def get_librarian_for_library(library_name):
    librarian = Library.objects.get(name=library_name).librarian
    return librarian