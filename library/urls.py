from django.urls import path
from .views import register, user_login, user_logout

from .views import book_list, add_book, edit_book, delete_book

from .views import borrow_book, return_book

from .views import submit_review

from .views import search_books

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    
    path('books/', book_list, name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    
    path('books/borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('books/return/<int:borrow_id>/', return_book, name='return_book'),
    path('books/review/<int:book_id>/', submit_review, name='submit_review'),
    path('books/search/', search_books, name='search_books'),
]

#urlpatterns += [  # Keep the authentication URLs]
