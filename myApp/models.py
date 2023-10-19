from collections.abc import Iterable
from django.contrib.auth.models import User
from django.db import models
from Users.models import CustomUser
from django.urls import reverse
import os
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField


def file_path(instance, filename):
    path = "documents/"
    format = "uploaded-" + filename
    return os.path.join(path, format)


class Bookbaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    kitob_name = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.url)

    def get_file_name(self):
        print("File name is ", self.file_upload.url)
        return str(self.file_upload.url).replace('documents/uploaded-', '')


class Dgubaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    dgu_name = models.ForeignKey('Certificate', on_delete=models.CASCADE, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.url)

    def get_file_name(self):
        print("File name is ", self.file_upload.url)
        return str(self.file_upload.url).replace('documents/uploaded-', '')

    
class Dissertationbaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    disser_name = models.ForeignKey('Dissertation', on_delete=models.CASCADE, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.url)


    def get_file_name(self):
        print("File name is ", self.file_upload.url)
        return str(self.file_upload.url).replace('documents/uploaded-', '')


class Maqolabaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    maqola_name = models.OneToOneField('Article', on_delete=models.CASCADE, null=True,)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.url)


    def get_file_name(self):
        print("File name is ", self.file_upload.url)
        return str(self.file_upload.url).replace('documents/uploaded-', '')
    
    def save(self, force_insert: bool = False, force_update: bool = False, using: str | None = None, update_fields: Iterable[str] | None = None) -> None:
        name = self.file_upload.name
        extension = name.split('.')[-1]
        for char in name:
            if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.':
                self.city_image.name = 'a' + '.' + extension
                break
        instance = super().save(force_insert=False, force_update=False, using=None,
                                          update_fields=None)
        # return super().save(force_insert, force_update, using, update_fields)


class Certificate(models.Model):
    cer_name = models.CharField(max_length=250, null=False)
    cer_muallif = models.CharField(max_length=250, null=False)
    date = models.CharField(max_length=200)
    dgunomer = models.CharField(max_length=20,  null=False, blank=True)
    application_number = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self):
        return self.cer_name
    
    def get_absolute_url(self):
        return reverse('cer_detail', args=[str(self.pk)])


class Article(models.Model):
    maq_name = models.CharField(max_length=250, null=False)
    maq_muallif = models.CharField(max_length=250, null=False)
    maq_nashr_sanasi = models.CharField(max_length=200)
    journal_name = models.CharField(max_length=250, null=False)
    volum = models.CharField(max_length=10, null=False, blank=True)
    issue = models.CharField(max_length=20, default='unknown')
    sahifalar = models.CharField(max_length=200, null=False)
    keywords = models.CharField(max_length=255, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.maq_name[:50]}..."
    
    def get_absolute_url(self):
        return reverse('artic_detail', args=[str(self.pk)])
    
    @property
    def get_keywords(self):
        return self.keywords.split(',')
    
    @property
    def get_article_references(self):
        return self.references.split(',')
    
    @property
    def get_article_file(self):
        return Maqolabaza.objects.filter(maqola_name=self.pk).first()


class Book(models.Model):
    book_name = models.CharField(max_length=250, null=False)
    book_muallif = models.CharField(max_length=250, null=False)
    book_nashr_sanasi = models.CharField(max_length=200)
    volume = models.CharField(max_length=20, null=False, blank=True)
    pages = models.CharField(max_length=20, null=False, blank=True)

    def __str__(self):
        return self.book_name
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.pk)])


class Dissertation(models.Model):
    dis_name = models.CharField(max_length=250, null=False)
    dis_muallif = models.CharField(max_length=250, null=False)
    dis_nashr_sanasi = models.CharField(max_length=200)
    institut = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self):
        return self.dis_name
    
    def get_absolute_url(self):
        return reverse('diss_detail', args=[str(self.pk)])


class FAQ(models.Model):
    STATUS = (
        ('True' , 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=300)
    answer = RichTextField(blank=True, null=True) 
    status = models.CharField(max_length=10, choices=STATUS)
    create_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    


