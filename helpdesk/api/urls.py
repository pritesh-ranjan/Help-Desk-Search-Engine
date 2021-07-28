from api import views
from django.urls import path

urlpatterns = [
    path('search/', views.SearchList.as_view()),
    # # Auth
    path('signup/', views.signup),
    path('login/', views.login),
]
