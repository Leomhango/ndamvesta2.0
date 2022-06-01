from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.index, name="logout"),
    path('search/', views.search, name="search")
]