from django.urls import path
from django.urls import include, re_path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    
]
