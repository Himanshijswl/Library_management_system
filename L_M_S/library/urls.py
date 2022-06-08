from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('view_book', views.view_book, name= 'view_book'),
    path('add_book', views.add_book, name= 'add_book'),
    path('update_book', views.update_book, name= 'update_book'),
    path('delete_book', views.delete_book, name= 'delete_book'),
    path('delete_book/<int:b_id>', views.delete_book, name= 'delete_book'),
    path('filter_book', views.filter_book, name= 'filter_book'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]
