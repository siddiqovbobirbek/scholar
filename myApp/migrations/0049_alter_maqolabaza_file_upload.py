# Generated by Django 4.1.7 on 2023-10-19 14:34

from django.db import migrations, models
import myApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0048_alter_bookbaza_file_upload_alter_dgubaza_file_upload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqolabaza',
            name='file_upload',
            field=models.FileField(storage=myApp.models.UTF8EncodedStorage(), upload_to='documents/'),
        ),
    ]
