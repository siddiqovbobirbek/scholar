from django.urls import path
from Users.views import register, login_view, logout_user, dashboard, profile_update
from myApp.views import index

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('index/', index, name="index"),
    path('logout/', logout_user, name="logout"),
    path('profile_update/', profile_update, name="profile_update"),
    path("filter/", index, name="index"),
    
]