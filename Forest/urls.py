from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as AuthViews
from django.urls import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('create/', PostCreatePage.as_view(template_name='create.html'), name='create'),
    path('update/<int:pk>/', PostUpdatePage.as_view(template_name='update.html'), name='update'),
    path('delete/<int:pk>/', PostDeletePage.as_view(template_name='delete.html'), name='delete'),
    path('post/<id>/', post_single, name='post'),
    path('author/<id>/', post_author, name='author'),
    path('search/', search, name='search'),
    path('like/<int:pk>/', likes, name='likes'),
]
