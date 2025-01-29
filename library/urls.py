from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  
    path('register/', views.register, name='register'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'), 
    path('add-book/', views.add_book, name='add_book'),
    path('media/<path:path>/', views.serve_pdf, name='serve_pdf'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('authors/', views.author_list, name='author_list'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/add/', views.add_author, name='add_author'),
    path('author/<int:pk>/edit/', views.edit_author, name='edit_author'),
    path('author/<int:pk>/delete/', views.delete_author, name='delete_author'),
]