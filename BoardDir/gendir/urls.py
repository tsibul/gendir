from django.urls import path
from . import views

app_name = 'gendir'

urlpatterns = [
    path('', views.index, name='index'),
]