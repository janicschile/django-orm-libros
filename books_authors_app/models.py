from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title}"
    def __str__(self):
        return f"{self.title}"

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255, default='Notas Aqui')
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"