from django.urls import path
from myApp.views import DGUView, DissertationView, BookView, MaqolaView
from .views import home, show_files, editor, book, dissertation, maqola, dgu, about, search, index

app_name = "myApp"

urlpatterns = [
    path("", home, name="home"),
    path("uploaddgu/", DGUView.as_view(), name="upload_dgu"),
    path("uploaddiss/", DissertationView.as_view(), name="upload_disser"),
    path("uploadbook/", BookView.as_view(), name="upload_book"),
    path("uploadmaq/", MaqolaView.as_view(), name="upload_maqola"),
    path("files/", show_files, name="show_files"),
    path("editor/", editor, name="editor"),
    path("dgu/", dgu, name="dgu"),
    path("maqola/", maqola, name="maqola"),
    path("book/", book, name="book"),
    path("dissertation/", dissertation, name="dissertation"),
    path("about/", about, name="about"),
    path("search/", search, name="search"),
    path("index/", index, name="index")
]