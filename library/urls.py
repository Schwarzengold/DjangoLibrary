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
]
