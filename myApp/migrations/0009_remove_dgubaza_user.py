# Generated by Django 4.1.7 on 2023-02-15 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_rename_data_certificate_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dgubaza',
            name='user',
        ),
    ]
