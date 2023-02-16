from django.urls import path
from Users.views import SignUpView
from Users.views import login

urlpatterns = [
    path('register/', SignUpView.as_view(), name="register"),
    path('login/', login, name="login"),
]