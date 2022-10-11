from email.policy import default
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    option_a = models.CharField(max_length=1000)
    option_b = models.CharField(max_length=1000)
    option_c = models.CharField(max_length=1000)
    option_d = models.CharField(max_length=1000)
    
class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key=True)
    answer = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.answer}" #"{self.question.question} \nA. {self.question.option_a}\nB. {self.question.option_b}\nC. {self.question.option_c}\nD. {self.question.option_d}\n Answer: {self.answer}"

class Respondance(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    responder = models.CharField(max_length=20)
    score = models.IntegerField()

