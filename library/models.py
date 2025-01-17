from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fantasy', 'Fantasy'),
        ('Science Fiction', 'Science Fiction'),
        ('Historical', 'Historical'),
        ('Adventure', 'Adventure'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Biography', 'Biography'),
        ('Poetry', 'Poetry'),
        ('Drama', 'Drama'),
    ]

    title = models.CharField(max_length=255)  
    author = models.CharField(max_length=255) 
    category = models.CharField(
        max_length=100, 
        choices=CATEGORY_CHOICES, 
        default='Fantasy'
    )
    description = models.TextField(blank=True)
    pdf_file = models.FileField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
