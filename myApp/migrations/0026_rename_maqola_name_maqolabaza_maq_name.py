# Generated by Django 4.1.7 on 2023-03-07 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0025_alter_maqolabaza_maqola_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maqolabaza',
            old_name='maqola_name',
            new_name='maq_name',
        ),
    ]