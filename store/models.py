from cmath import e
from django.db import models

# Create your models here.


class Author(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 255)
    dob = models.DateField(default = None)


    
    

    def __str__(self):
        return self.firstName

#an author can have many books, but a book can have only one author
#one to many relationship

class Book(models.Model):
    title = models.CharField(max_length = 255)
    YearOfPublication = models.DateField(default = None)
    description = models.CharField(max_length = 255)
    date_added = models.DateTimeField(auto_now_add = True)
    author_id = models.ForeignKey(Author, on_delete = models.SET_NULL, related_name = "authors", null=True)
    # author = models.ForeignKey(Author, to_field='id', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.author_id.firstName





    

class Stock (models.Model):
    book_id = models.ForeignKey(Book, on_delete = models.SET_NULL, related_name = "books", null=True)
    status = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.book_id.title

    