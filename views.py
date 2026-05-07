from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Score
from .forms import RegisterForm


# REGISTER
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


# LOGIN
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")

    return render(request, "login.html", {"form": form})

# HOME
@login_required
def home(request):
    return render(request, "home.html")


# PLAY
@login_required
def play(request):
    return render(request, "play.html")


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("login")


# LEADERBOARD
def leaderboard(request):
    scores = Score.objects.all().order_by("-score")[:10]
    return render(request, "leaderboard.html", {"scores": scores})


# SAVE SCORE
@csrf_exempt
def save_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        score = data.get("score")

        if request.user.is_authenticated:
            Score.objects.create(
                username=request.user.username,
                score=score
            )
            return JsonResponse({"status": "success"})
        
        return JsonResponse({"status": "not_logged_in"})

    return JsonResponse({"status": "invalid"})