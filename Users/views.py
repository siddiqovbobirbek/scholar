from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    form = RegisterForm()
    context = {'form': form}
    if request.method == "POST":
        print("Request post, on register")
        form = RegisterForm(request.POST)
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
            new_user = authenticate(username=username, first_name=first_name, 
                last_name=last_name, email=email, 
                age=age, address=address, job=job, 
                number=number, password1=password1, 
                password2=password2)
            print("Authenticated user")
            login(request, new_user)
            return redirect("register")
    else:
        form = RegisterForm()
    return render(request, "register.html", context)

# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             new_user = authenticate(username=username, password=password)
#             if new_user is not None:
#                 login(request, new_user)
#                 return redirect('register')
#     else:
#         form = CustomUserCreationForm()
#     context = {'form': form}
#     return render(request, 'register.html', context)



def login(request):
    if request.method == "POST":
        email = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    else:
        messages.error(request, "Invalid email or password")
    return render(request, "login.html")