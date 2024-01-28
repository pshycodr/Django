from django.urls import path
from . import views
from HomePage.views import home

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]

