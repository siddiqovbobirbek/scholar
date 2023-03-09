from django.urls import path
from myApp.views import DGUView, DissertationView, BookView, MaqolaView
from .views import home, editor, book, dissertation, maqola, dgu, about, search, index, faq_view, book_detail, cer_detail, artic_detail, diss_detail

app_name = "myApp"

urlpatterns = [
    path("", home, name="home"),
    path("uploaddgu/", DGUView.as_view(), name="upload_dgu"),
    path("uploaddiss/", DissertationView.as_view(), name="upload_disser"),
    path("uploadbook/", BookView.as_view(), name="upload_book"),
    path("uploadmaq/", MaqolaView.as_view(), name="upload_maqola"),
    path("editor/", editor, name="editor"),
    path("dgu/", dgu, name="dgu"),
    path("maqola/", maqola, name="maqola"),
    path("book/", book, name="book"),
    path("dissertation/", dissertation, name="dissertation"),
    path("about/", about, name="about"),
    path("search/", search, name="search"),
    path("index/", index, name="index"),
    path("faq/", faq_view, name="faq"),
    path('detail/book/<int:pk>/', book_detail, name='book_detail'),
    path('detail/cer/<int:pk>/', cer_detail, name='cer_detail'),
    path('detail/artic/<int:pk>/', artic_detail, name='artic_detail'),
    path('detail/diss/<int:pk>/', diss_detail, name='diss_detail'),
]