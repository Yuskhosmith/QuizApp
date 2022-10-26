from tkinter.messagebox import NO
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import Question, Respondance, User, Quiz, Answer
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
def index(request):
    try:
        user_id=request.user.id
        if user_id is not None:

            q = Quiz.objects.filter(user=user_id)
            return render(request, "quizapp/index.html", {
                'tests': q
            })
        return render(request, "quizapp/landingpage.html")
    except:
        return render(request, "quizapp/landingpage.html")

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
def delete(request, test_id):
    if request.method == "POST":        
        test = Quiz.objects.get(id=test_id)
        user = User.objects.get(id=request.user.id)
        item = Quiz.objects.filter(user=user, title=test.title)
        item.delete()
        return render(request, "quizapp/deleted.html", {
            "test": test
        })
    return HttpResponseRedirect("/tests/" + str(test_id))
    

@login_required(login_url='/login')
def createtest(request):
    if request.method == "POST":
        try:
            user = User.objects.get(id=request.user.id)
            title = request.POST["title"]
            description = request.POST["description"]

            # Ensuring all items are filled
            items = [title, description]
            for i in items:
                if len(i) < 1:
                    break #Implement in Js and remove it here

            # Attempt to create new test
            try:
                test = Quiz.objects.create(user=user, title=title, description=description)
                test.save()
                saved_test = Quiz.objects.filter(user=user, title=title, description=description).first()
                
                return HttpResponseRedirect("/tests/" + str(saved_test.id)) 
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
    quiz = Quiz.objects.get(id=test_id)
    availableQuestions = len(Question.objects.filter(quiz=quiz))
    

    # Submit question for quiz
    if request.method == "POST":
        try:
            question = request.POST["question"]
            option_a = request.POST["option_a"]
            option_b = request.POST["option_b"]
            option_c = request.POST["option_c"]
            option_d = request.POST["option_d"]

            qstn = Question.objects.create(quiz=quiz, question=question, option_a=option_a, option_b=option_b, option_c=option_c, option_d=option_d)
            qstn.save()
        except ValueError:
            return render(request, "quizapp/test.html", {
                "test": Quiz.objects.get(id=test_id),
            })
        answer = request.POST["answer"]
        qstnAns = Answer.objects.create(question=qstn, answer=answer)
        qstnAns.save()
        
        return HttpResponseRedirect("/tests/" + str(test_id))
    else:
        questions = Question.objects.filter(quiz=quiz)
        responders = Respondance.objects.filter(quiz=quiz)
        
               
        return render(request, "quizapp/test.html", {
            "questions": questions,
            "test": quiz,
            "noq": availableQuestions,
            "responders": responders,

        })

def takequiz(request):
    if request.method == "POST":
        try:
            quizid = request.POST["quizid"]
            quiztaker = request.POST["quiztaker"]
            quiz = Quiz.objects.get(id=quizid)
        except:
            return render(request, "quizapp/dne.html", {
                "message": "Ensure you input the correct Test ID"
            })
        return render(request, "quizapp/quiz.html", {
            "quizid": quizid,
            "quiztaker": quiztaker,
            "questions": Question.objects.filter(quiz=quiz),
            "test": quiz,
        })
    return render(request, "quizapp/takequiz.html")


def submit(request):
    if request.method == "POST":
        try:
            quizid = request.POST["quizid"]
            quiztaker = request.POST["quiztaker"]
            quiz = Quiz.objects.get(id=quizid)
            questions = Question.objects.filter(quiz=quiz)
            score = 0
            for question in questions:
                sol = request.POST[f"{question.id}"]
                rsol = question.answer
                if str(sol) == str(rsol):
                    score += 1
                    # print(sol, rsol, score)
            respondance = Respondance.objects.create(quiz=quiz, responder=quiztaker, score=score)
            respondance.save()
        except:
            return HttpResponseRedirect("/takequiz/")
        return render(request, "quizapp/complete.html", {
            "name": quiztaker,

        })
                
    return HttpResponseRedirect("/takequiz/")