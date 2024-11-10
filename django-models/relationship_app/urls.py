from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_all_books, name="home"),
    path("", views.LibraryDetailsView, name="home"),
]
