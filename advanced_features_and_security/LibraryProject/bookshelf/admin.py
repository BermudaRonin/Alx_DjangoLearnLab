from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_of_birth")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "date_of_birth",
                    "profile_photo",
                ),
            },
        ),
    )
    search_fields = ("username", "email", "date_of_birth")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
