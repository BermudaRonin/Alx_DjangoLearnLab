from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


def list_all_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "list_books.html", context)

class LibraryDetailsView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object() 
        context['average_rating'] = book.get_average_rating()