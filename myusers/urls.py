from django.contrib import admin
from django.urls import path
from  django.contrib.auth import views as auth_views
from myusers import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    # path('show',views.show,name='show'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    # path('add/', views.add,name='show')   
]

