from django.contrib import admin
from myApp.models import Certificate, Article, Book, Dissertation, Bookbaza, Dgubaza, Dissertationbaza, Maqolabaza, FAQ

@admin.register(Bookbaza)
class BookbazaAdmin(admin.ModelAdmin):
    list_display = ("id", "kitob_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")


@admin.register(Dgubaza)
class DgubazaAdmin(admin.ModelAdmin):
    list_display = ("id", "dgu_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")


@admin.register(Maqolabaza)
class MaqolabazaAdmin(admin.ModelAdmin):
    list_display = ("id", "maqola_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")


@admin.register(Dissertationbaza)
class DissertationbazaAdmin(admin.ModelAdmin):
    list_display = ("id", "disser_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "cer_name", "cer_muallif", "date", "dgunomer")
    list_display_links = ("cer_muallif", "dgunomer")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "maq_name", "maq_muallif", "journal_name", "maq_nashr_sanasi")
    list_display_links = ("maq_muallif", "journal_name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "book_name", "book_muallif", "book_nashr_sanasi", "pages")
    list_display_links = ("book_name", "book_muallif")


@admin.register(Dissertation)
class DissertationAdmin(admin.ModelAdmin):
    list_display = ("id", "dis_name", "dis_muallif", "dis_nashr_sanasi",)
    list_display_links = ("dis_name", "dis_muallif")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "ordernumber", "question", "answer", "status")
    list_display_links = ("status", "answer")