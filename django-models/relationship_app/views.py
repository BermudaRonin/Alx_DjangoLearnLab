from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
# from .forms import BookForm

# Task 1 : Django Views and URL Configuration

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Task 2 : Implementing User Authentication in Django

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Task 3 : Implement Role-Based Access Control in Django

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

admin_view = user_passes_test(is_admin)
librarian_view = user_passes_test(is_librarian)
member_view = user_passes_test(is_member)

@admin_view
def admin_view(request):
    return render(request, 'admin_view.html')

@librarian_view
def librarian_view(request):
    return render(request, 'librarian_view.html')

@member_view
def member_view(request):
    return render(request, 'member_view.html')


# @permission_required('relationship_app.can_add_book', raise_exception=True)
# def add_book(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'relationship_app/book_form.html', {'form': form})


# @permission_required('relationship_app.can_change_book', raise_exception=True)
# def edit_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'relationship_app/book_form.html', {'form': form})

# @permission_required('relationship_app.can_delete_book', raise_exception=True)
# def delete_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == "POST":
#         book.delete()
#         return redirect('book_list')
#     return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})