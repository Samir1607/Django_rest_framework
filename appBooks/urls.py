from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books_list/', views.books_list, name='books_list'),
    path('samir/', views.samir, name='samir'),
    path('add_book/', views.add_book, name="add_book"),
    path('book/<int:pk>', views.book, name="book"),
]
