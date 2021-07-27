from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('search/', views.SeearchList.as_view()),
    # # Auth
    path('signup', views.signup),
    path('login', views.login),
]
