from QuizApp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    # path('addQuestion/', addQuestion,name='addQuestion'),
    # path('login/', loginPage,name='login'),
    # path('logout/', logoutPage,name='logout'),
    # path('register/', registerPage,name='register'),
 
]