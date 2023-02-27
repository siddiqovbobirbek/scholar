from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout



def register(request):
    form = RegisterForm()
    context = {'form': form}
    print("Req data", request)
    print("Req user", request.user)
    if request.method == "POST":
        print("Request post, on register")
        form = RegisterForm(request.POST)
        print("\n\n", "form.errors:", form.errors, "\n\n")
        print("Form data", form.cleaned_data)
        if form.is_valid():
            print("Xato yo'q. Forma to'g'ri ")
            form.save()
            username = form.cleaned_data.get("username")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            age = form.cleaned_data.get("age")
            address = form.cleaned_data.get("address")
            job = form.cleaned_data.get("job")
            number = form.cleaned_data.get("number")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            print("forma saqlandi. Register forma")
            new_user = authenticate(username=username, password=password2)
            if new_user is not None:
                print("Authenticated user")
                login(request, new_user)
                messages.error(request, form.errors)
            else:
                return render(request, "register.html", context)
            return redirect("index")
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = RegisterForm()
        messages.error(request, form.errors)
        print(form.errors)
    return render(request, "register.html", context)



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    else:
        messages.error(request, "Invalid email or password")
    return render(request, "login.html")


def dashboard(request):
    return render(request, "dashboard.html")


def logout_user(request):
    logout(request)
    return redirect('myApp:home')