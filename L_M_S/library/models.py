from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 100, null =False)
    location = models.CharField(max_length = 100)
    age = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100, null = False)
    subject = models.CharField(max_length=100)
    price = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return "%s %s" %(self.name,self.author)