from django.urls import path
from myApp.views import DGUView, DissertationView, BookView, MaqolaView
from .views import home, editor, book, dissertation, maqola, dgu, about, search, index, faq_view, book_detail, cer_detail, artic_detail, diss_detail, archives_list, archive_detail, add_archive, edit_archive, delete_archive

app_name = "myApp"

urlpatterns = [
    path("", home, name="home"),
    path("uploaddgu/<int:certificate_id>/", DGUView.as_view(), name="upload_dgu"),
    path("uploaddiss/<int:dissertation_id>/", DissertationView.as_view(), name="upload_disser"),
    path("uploadbook/<int:book_id>/", BookView.as_view(), name="upload_book"),
    path("uploadmaq/<int:maqola_id>/", MaqolaView.as_view(), name="upload_maqola"),
    path("editor/", editor, name="editor"),
    path("patent/", dgu, name="dgu"),
    path("article/", maqola, name="maqola"),
    path("book/", book, name="book"),
    path("dissertation/", dissertation, name="dissertation"),
    path("about/", about, name="about"),
    path("search/", search, name="search"),
    path("filter/", index, name="index"),
    path("faq/", faq_view, name="faq"),
    path('detail/book/<int:pk>/', book_detail, name='book_detail'),
    path('detail/cer/<int:pk>/', cer_detail, name='cer_detail'),
    path('detail/artic/<int:pk>/', artic_detail, name='artic_detail'),
    path('detail/diss/<int:pk>/', diss_detail, name='diss_detail'),
    
    path('archives/', archives_list, name='archives_list'),
    path('archives/<int:pk>/', archive_detail, name='archive_detail'),
    path('archives/add/', add_archive, name='add_archive'),
    path('archives/edit/<int:pk>/', edit_archive, name='edit_archive'),
    path('archives/delete/<int:pk>/', delete_archive, name='delete_archive'),
]