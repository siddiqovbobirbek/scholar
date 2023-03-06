# Generated by Django 4.1.7 on 2023-03-06 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_alter_faq_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='muallif',
            new_name='maq_muallif',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='maq_name',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='nashr_sanasi',
            new_name='maq_nashr_sanasi',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='muallif',
            new_name='book_muallif',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='nashr_sanasi',
            new_name='book_nashr_sanasi',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='muallif',
            new_name='cer_muallif',
        ),
        migrations.RenameField(
            model_name='certificate',
            old_name='name',
            new_name='cer_name',
        ),
        migrations.RenameField(
            model_name='dissertation',
            old_name='muallif',
            new_name='dis_muallif',
        ),
        migrations.RenameField(
            model_name='dissertation',
            old_name='name',
            new_name='dis_name',
        ),
    ]