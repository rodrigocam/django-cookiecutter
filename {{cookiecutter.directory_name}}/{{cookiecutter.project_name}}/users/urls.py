from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, register


urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.login, {'template_name': 'users/login.jinja2'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'index'}, name='logout'),
    path('register/', register, name='register'),
]
