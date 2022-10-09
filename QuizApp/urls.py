from unicodedata import name
from QuizApp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createtest", views.createtest, name="createtest"),
    path("tests", views.tests, name="tests"),
    path("test/<int:test_id>", views.tests, name="test"),
    # path('addQuestion/', addQuestion,name='addQuestion'),
 
]