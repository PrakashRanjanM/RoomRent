from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('services', views.services , name = "services"),
    path('about', views.about , name = "about"),
    path('wishlist', views.wishlist , name = "wishlist"),
    path('search', views.search , name = "search"),
    path('contact', views.contact , name = "contact"),
    path('help', views.help , name = "help"),
    path('signup', views.handleSignUp , name = "signup"),
    path('login', views.handleLogIn , name='logIn'),
    path('LYF', views.lyf , name='LYF'),
    path('logout', views.handleLogOut , name='logOut'),

]