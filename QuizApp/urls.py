from QuizApp import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    # path('addQuestion/', addQuestion,name='addQuestion'),
    # path('login/', loginPage,name='login'),
    # path('logout/', logoutPage,name='logout'),
    # path('register/', registerPage,name='register'),
 
]