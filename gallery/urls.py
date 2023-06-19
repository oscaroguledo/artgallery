from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.GalleryView.as_view(),name='view-gallery'),
    path('filter_gallery/', views.GalleryFilter.as_view(),name='filter-gallery'),
    #path('logout/', views.logout, name='logout'),
    #path('reset_password/', views.reset_password, name='reset_password'),
]