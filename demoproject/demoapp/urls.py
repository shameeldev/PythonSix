
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('details/', views.details,name='details'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('thanks/', views.thanks,name='thanks'),
    path('details/operations/', views.operations,name='operations')
]