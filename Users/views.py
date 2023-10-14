from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import  RegisterForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from .models import CustomUser

from django.contrib.auth.decorators import login_required

from django.utils.html import strip_tags


def register(request):
    form = RegisterForm()
    context = {'form': form}
    # print("Req data", request)
    # print("Req user", request.user)
    if request.method == "POST":
        # print("Request post, on register")
        form = RegisterForm(request.POST)
        # print("\n\n", "form.errors:", form.errors, "\n\n")
        # print("Form data", form.cleaned_data)
        if form.is_valid():
            # print("Xato yo'q. Forma to'g'ri ")
            try:
                form.save()
                messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz.")
            except Exception as e:
                # messages.error(request, "Xatolik yuz berdi. Iltimos qayta urinib ko'ring.")
                messages.error(request, form.errors)
                return render(request, "register.html", context)
            username = form.cleaned_data.get("username")
            # first_name = form.cleaned_data.get("first_name")
            # last_name = form.cleaned_data.get("last_name")
            # email = form.cleaned_data.get("email")
            # age = form.cleaned_data.get("age")
            # address = form.cleaned_data.get("address")
            # job = form.cleaned_data.get("job")
            # number = form.cleaned_data.get("number")
            # password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            # print("forma saqlandi. Register forma")
            new_user = authenticate(username=username, password=password2)
            if new_user is not None:
                # print("Authenticated user")
                login(request, new_user)
                messages.error(request, form.errors)
            else:
                return render(request, "register.html", context)
            return redirect("index")
        else:
            messages.error(request, form.errors)
    else:
        form = RegisterForm()
        messages.error(request, form.errors)
        # print(form.errors)
    return render(request, "register.html", context)



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "":
            messages.error(request, "Iltimos, foydalanuvchi nomini kiriting.")
            return redirect("login")
        elif password == "":
            messages.error(request, "Iltimos, parolni kiriting.")
            return redirect("login")
        if not CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Bunday foydalanuvchi mavjud emas.")
            return redirect("login")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Username yoki parol xato")
    return render(request, "login.html")




@login_required
def dashboard(request):
    return render(request, "dashboard.html")


def logout_user(request):
    logout(request)
    return redirect('myApp:home')


@login_required
def profile_update(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)
    else:
        profile_form = ProfileForm(instance=request.user) 
    context = {
        'profile_form': profile_form
    }
    return render(request, "profile_update.html", context)