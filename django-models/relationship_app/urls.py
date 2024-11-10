from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("", list_books, name="home"),
    path("", LibraryDetailView, name="home"),
]
