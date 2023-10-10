# Generated by Django 4.1.7 on 2023-10-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0042_article_abstract_article_keywords_article_references'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
