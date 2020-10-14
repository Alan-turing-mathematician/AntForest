from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as AuthViews
from django.urls import include

urlpatterns = [
	path('admin/', admin.site.urls),
    path('register/', register_page, name='register'),
    path('login/', AuthViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', AuthViews.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<id>/', profile, name='profile')
]
