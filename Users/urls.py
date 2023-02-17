from django.urls import path
from Users.views import register
from Users.views import login

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
]