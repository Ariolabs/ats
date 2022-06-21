from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .api import UserAPI
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path("logout", auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register', views.register, name='register'),
    path('api/', UserAPI.as_view(), name='userapi'),

]   