from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # owner
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    published_year = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)  # many-to-many

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.pk})

class Note(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Note on {self.book.title} ({self.created_at:%Y-%m-%d})'
