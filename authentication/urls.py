from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', auth_views.LoginView.as_view(template_name='authentication/login.html'),name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'),name='login'),
    path('logout/', views.logout, name='logout'),
    #path('reset_password/', views.reset_password, name='reset_password'),
]