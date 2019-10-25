from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('games/', views.games, name='games'),
    path('ksjof/', views.ksjof, name='ksjof'),
    path('sftc/', views.sftc, name='sftc'),
    path('messagecomplete/', views.messagecomplete, name='messagecomplete'),
    path('contact/', views.contact, name='contact'),
   # path('email/', views.email, name='email'),


    # path('', views.index, name='index'),

]
