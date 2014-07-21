from django.db import models
from django.contrib import admin

class Book(models.Model):
    name = models.CharField(max_length=100)
    year_of_book = models.CharField(max_length=4)
    department = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/pic_folder')
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

admin.site.register(Book)

# Create your models here.
