# Generated by Django 4.1.7 on 2023-03-03 08:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_alter_faq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
