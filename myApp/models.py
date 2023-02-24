from django.contrib.auth.models import User
from django.db import models
from Users.models import CustomUser
import os
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor_uploader.fields import RichTextUploadingField


def file_path(instance, filename):
    path = "documents/"
    format = "uploaded-" + filename
    return os.path.join(path, format)


class Bookbaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.name)

    def get_file_name(self):
        print("File name is ", self.file_upload.name)
        return str(self.file_upload.name).replace('documents/uploaded-', '')


class Dgubaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.name)

    def get_file_name(self):
        print("File name is ", self.file_upload.name)
        return str(self.file_upload.name).replace('documents/uploaded-', '')

    
class Dissertationbaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.name)


    def get_file_name(self):
        print("File name is ", self.file_upload.name)
        return str(self.file_upload.name).replace('documents/uploaded-', '')


class Maqolabaza(models.Model):
    file_upload = models.FileField(upload_to=file_path)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.file_upload.name)


    def get_file_name(self):
        print("File name is ", self.file_upload.name)
        return str(self.file_upload.name).replace('documents/uploaded-', '')


class Certificate(models.Model):
    name = models.CharField(max_length=100, null=False)
    muallif = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(default=timezone.now)
    dgunomer = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100, null=False)
    muallif = models.CharField(max_length=100, null=False)
    journal_name = models.CharField(max_length=100, null=False)
    nashr_sanasi = models.DateField()
    bob = models.CharField(max_length=100, null=False)
    number = models.IntegerField(null=False)
    sahifalar = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    muallif = models.CharField(max_length=100, null=False)
    nashr_sanasi = models.DateField()
    nashriyot_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dissertation(models.Model):
    name = models.CharField(max_length=100, null=False)
    muallif = models.CharField(max_length=100, null=False)
    yunalish = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    STATUS = (
        ('True' , 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=300)
    answer = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question