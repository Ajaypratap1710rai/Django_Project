from django.urls import path
from .views import home, register, user_login, user_logout, create_post

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create_post/', create_post, name='create_post'),
]
