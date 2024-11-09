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
    librarian = Library.objects.get(name=library_name)
    return librarian
