from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('loginpage/', views.loginpage, name="loginpage"),
    
    path('signuppage/', views.signuppage, name="signuppage"),
    path('logoutPage/', views.logoutPage, name="logoutPage"),
    path('adminpage/', views.adminpage, name="adminpage"),
    path('profile/', views.Profile, name="profile"),
    path('newspost/', views.NewsPost, name="newspost"),
    path('addmembers/', views.AddMembers, name="addmembers"),
    path("newsuserview/", views.NewsUserView, name="newsuserview"),
    path("userform/", views.UserRegisterForm, name="userform"),
    path("update/<int:id>/", views.view_profile, name="edit"),
    path("event/", views.Event, name="event"),
    
    
]