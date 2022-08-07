from django.urls import path, re_path
from . import  views
from django.contrib.auth import views as auth_views

app_name = 'gendir'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/logout/', auth_views.LogoutView.as_view()),
    path('accounts/logout-then-login/', auth_views.logout_then_login),
    path('new_task', views.new_task, name='new_task'),
    path('add_task', views.add_task, name='add_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('edit_task/update_task/<int:id>', views.update_task, name='update_task'),

]