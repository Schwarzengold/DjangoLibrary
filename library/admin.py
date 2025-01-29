from django.contrib import admin
from .models import Book, Author

admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('category',)
