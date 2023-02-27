from django.urls import path
from Users.views import register
from Users.views import login_view, logout_user, dashboard
from myApp.views import index

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('index/', index, name="index"),
    path('logout/', logout_user, name="logout"),
    # path('profile/', profile, name="profile"),
    path('dashboard/', dashboard, name="dashboard")
    
]