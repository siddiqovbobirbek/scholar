from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('myApp:home')
    template_name = "register.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            form.save()
            new_user = authenticate(username=username, email=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("register")
    else:
        form = CustomUserCreationForm()
        
        context = {
            "form":form
        }
    return render(request, "register.html", context)

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error":"Invalid username or password."}
            return render(request, "login.html", context)
        login(request, user)
        return redirect("/")
    context = {}
    return render(request, "login.html", context)