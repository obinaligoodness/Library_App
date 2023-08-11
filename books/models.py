from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),
        ('ROMANCE', 'Romance')
    ]
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=11, choices=GENRE_CHOICES, default="Finance")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateField(blank=True, null=True)
    copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.isbn}"

    class Meta:
        ordering = ['title']


class Address(models.Model):
    house_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="Nigeria")


class BookInstance(models.Model):
    book = models.OneToOneField(Book, on_delete=models.PROTECT, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_borrowed = models.DateField(auto_now_add=True)
    date_returned = models.DateField()


class ReviewModel(models.Model):
    DESCRIPTION_CHOICES = [
        ('INTRESTING', 'Intresting'),
        ('SWEET', 'Sweet'),
        ('BORING', 'Boring'),
    ]
    reviewer_name = models.CharField(max_length=200)
    book = models.ManyToOneRel(Book, on_delete=models.CASCADE,to=Book,field_name='book')
    description = models.CharField(max_length=15,choices=DESCRIPTION_CHOICES,default='intresting')
