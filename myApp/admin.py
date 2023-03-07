from django.contrib import admin
from myApp.models import Certificate, Article, Book, Dissertation, Bookbaza, Dgubaza, Dissertationbaza, Maqolabaza, FAQ

@admin.register(Bookbaza)
class BookbazaAdmin(admin.ModelAdmin):
    list_display = ("kitob_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")

@admin.register(Dgubaza)
class DgubazaAdmin(admin.ModelAdmin):
    list_display = ("dgu_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")


@admin.register(Maqolabaza)
class MaqolabazaAdmin(admin.ModelAdmin):
    list_display = ("maqola_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")


@admin.register(Dissertationbaza)
class DissertationbazaAdmin(admin.ModelAdmin):
    list_display = ("disser_name", "upload_date", "file_upload",)
    list_display_links = ("file_upload", "upload_date")

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("cer_name", "cer_muallif", "date", "dgunomer")
    list_display_links = ("cer_muallif", "dgunomer")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("maq_name", "maq_muallif", "journal_name", "maq_nashr_sanasi")
    list_display_links = ("maq_muallif", "journal_name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("book_name", "book_muallif", "book_nashr_sanasi", "nashriyot_name")
    list_display_links = ("book_name", "book_muallif")


@admin.register(Dissertation)
class DissertationAdmin(admin.ModelAdmin):
    list_display = ("dis_name", "dis_muallif", "yunalish")
    list_display_links = ("dis_name", "dis_muallif", "yunalish")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("ordernumber", "question", "answer", "status")
    list_display_links = ("status", "answer")