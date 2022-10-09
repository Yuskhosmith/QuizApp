from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Quiz
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
def index(request):

    return render(request, "quizapp/index.html", {
        'tests': Quiz.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "quizapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "quizapp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            email = request.POST["email"]

            # Ensure password matches confirmation
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            if password != confirmation:
                return render(request, "quizapp/register.html", {
                    "message": "Passwords must match."
                })
            elif len(password) < 8:
                return render(request, "quizapp/register.html", {
                    "message": "Password cannot be less than 8 characters."
                })

            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                return render(request, "quizapp/register.html", {
                    "message": "Username already taken."
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        except ValueError:
            return render(request, "quizapp/register.html", {
                "message": "All Field must be set"
            })
    else:
        return render(request, "quizapp/register.html")

@login_required(login_url='/login')
def createtest(request):
    if request.method == "POST":
        try:
            user = User.objects.get(id=request.user.id)
            title = request.POST["title"]
            description = request.POST["description"]
            number_of_questions = request.POST["number_of_questions"]
            duration = request.POST["duration"]

            # Ensuring all items are filled
            items = [title, description, number_of_questions, duration]
            for i in items:
                if len(i) < 1:
                    break #Implement in Js and remove it here

            # Attempt to create new test
            try:
                test = Quiz.objects.create(user=user, title=title, description=description, number_of_questions=number_of_questions, duration=duration)
                test.save()
                saved_test = Quiz.objects.filter(user=user, title=title, description=description, number_of_questions=number_of_questions, duration=duration).first()
                
                return HttpResponseRedirect("/tests/" + saved_test.id) 
                """render(request, "quizapp/test.html", {
                    'x': saved_test,
                    'y': saved_test.id,
                    'z': test.id,
                }""" 
                #HttpResponseRedirect("/tests/" + saved_test.id) 
            except IntegrityError:
                return render(request, "quizapp/createtest.html", {
                    "message": "Title already exist."
                })
            
        except ValueError:
            pass
    else:
        return render(request, "quizapp/createtest.html")


@login_required(login_url='/login')
def tests(request, test_id):
    
    return render(request, "quizapp/test.html", {
        "test": Quiz.objects.get(id=test_id),
    })