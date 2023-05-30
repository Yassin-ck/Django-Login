from . import views
from django.urls import path

urlpatterns = [
    path('',views.Register,name='register'),
    path('login',views.Login,name='login'),
    path('home',views.Home,name='home'),
    path('logout',views.Logout,name='logout'),
]