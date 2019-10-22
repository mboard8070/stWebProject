from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('games/', views.games, name='games'),
    path('contact/', views.contact, name='contact'),
    path('ksjof/', views.ksjof, name='ksjof'),
    path('sftc/', views.sftc, name='sftc'),
    # path('', views.index, name='index'),
]
