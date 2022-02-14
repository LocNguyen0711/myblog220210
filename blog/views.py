from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import mCreatepost
from .forms import fUserCreate, fCreatepost
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.


def index(request):
     getPost = mCreatepost.objects.all()
     return render(request, "pages/index.html", {
          "posts": getPost
     })

def newpost(request):
     if not request.user.is_authenticated:
          return HttpResponseRedirect(reverse("blog:signin_view"))
     if request.method == "POST":
          form = fCreatepost(request.POST)
          if form.is_valid():
               saveForm = mCreatepost(title = form.cleaned_data["title"], discription = form.cleaned_data["discription"], body = form.cleaned_data["body"])
               saveForm.save()
               return render(request, "pages/newpost.html", {
                    "form": fCreatepost()
               })
          else:
               return render(request, "pages/newpost.html", {
                    "form": form
               })
     return render(request, "pages/newpost.html", {
          "form": fCreatepost()
     })

def profit(request):
     if not request.user.is_authenticated:
          return HttpResponseRedirect(reverse("blog:signin_view"))
     return render(request, "pages/profit.html")

def contact(request):
     return render(request, "pages/contact.html")

def signin_request(request):
     if request.method == "POST":
          username = request.POST["username"]
          password = request.POST["password"]
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request, user)
               return HttpResponseRedirect(reverse("blog:index"))
          else:
               return render(request, "pages/signin.html", {
                    "message": "The username or password is incorrect!"
               })
     return render(request, "pages/signin.html")

def signup_request(request):
     if request.method == "POST":
          form = fUserCreate(request.POST)
          if form.is_valid():
               username = form.cleaned_data["username"]
               password = form.cleaned_data["password1"]
               form.save()
               new_user = authenticate(username=username, password=password)
               if new_user is not None:
                    login(request, new_user)
                    return HttpResponseRedirect(reverse("blog:index"))
               else:
                    return render(request, "pages/signup.html", {
                         "form": form
                    })
          else:
               return render(request, "pages/signup.html", {
                    "form": form

               })
     return render(request, "pages/signup.html", {
          "form": fUserCreate()
     })
def signout_request(request):
     logout(request)
     return HttpResponseRedirect(reverse("blog:index"))
 