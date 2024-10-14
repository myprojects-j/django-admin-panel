from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self) -> str:
        return self.name


class Author1(models.Model):
    author_name=models.CharField(max_length=100)
    book_name=models.CharField(max_length=200)
    book_price=models.IntegerField(default=100)


    def __str__(self) -> str:
        return self.book_name


class Destinations(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc= models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.desc