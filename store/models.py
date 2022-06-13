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

    '''@property
    def is_out_of_stock(self):
        return self.quantity > 0 '''



    '''@property
    def status(self):
            if self.quantity<=0:
                stock_status = "out of stock"
            elif self.quantity<=5 and self.quantity>=1:
                stock_status ="critical"
            elif self.quantity<=10 and self.quantity>=5:
                stock_status ="bad"
            else:
                stock_status ="good"

            return stock_status'''

class Stock (models.Model):
    CHOICES =(('out of stock','out of stock'),
    ('critical','critical'),
    ('good','good'),
    ('bad','bad'))
    book_id = models.ForeignKey(Book, on_delete = models.SET_NULL, related_name = "books", null=True)
    status = models.CharField(max_length=255, choices=CHOICES)
    date_added = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.book_id.title

    