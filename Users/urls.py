from django.urls import path
from Users.views import register
from Users.views import login
from myApp.views import index, book, dissertation, maqola, dgu

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('index/', index, name="index"),
    path("dgu/", dgu, name="dgu"),
    path("maqola/", maqola, name="maqola"),
    path("book/", book, name="book"),
    path("dissertation/", dissertation, name="dissertation"),
]