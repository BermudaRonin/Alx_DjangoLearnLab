from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publication_year = models.IntegerField()


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, date_of_birth, profile_photo=None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, date_of_birth, profile_photo=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        permissions=[
            ('can_view', 'can view article'),
            ('can_create', 'can create article'),
            ('can_edit', 'can edit article'),
            ('can_delete', 'can delete article'),
        ]   
    