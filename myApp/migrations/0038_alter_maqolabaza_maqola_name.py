# Generated by Django 4.1.7 on 2023-03-13 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0037_alter_bookbaza_kitob_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqolabaza',
            name='maqola_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.article'),
        ),
    ]
