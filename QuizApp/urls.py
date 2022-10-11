from QuizApp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createtest", views.createtest, name="createtest"),
    path("delete/<int:test_id>", views.delete, name="delete"),
    path("tests", views.index, name="index"),
    path("tests/<int:test_id>", views.tests, name="tests"),
    path("takequiz/", views.takequiz, name="takequiz"),
    path("takequiz/submit", views.submit, name="submit"),
]