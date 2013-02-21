from shop.models import Product
from django.db import models

class Book(Product):
    TYPE_CHOICES = (
        ('1', 'Audio Book'),
        ('2', 'Ebook'),
        ('3', 'Book'),
      
    )
    isbn = models.CharField(max_length=255)
    #type = models.CharField(max_length=255,choices=TYPE_CHOICES)
    class Meta: pass