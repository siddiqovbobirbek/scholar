from django.urls import path
from Users.views import register
from Users.views import login
from myApp.views import index

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    
]