from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    # not logged in
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),

    # logged in
    path('home/', views.home, name="home"),
    path('post/', views.addWord, name="post"),
    path('results/', views.results, name="results"),
    path('dashboard/', views.dashbBoard, name="dashboard"),

    # authentication
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

]