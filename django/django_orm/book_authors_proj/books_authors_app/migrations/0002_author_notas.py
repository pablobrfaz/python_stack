# Generated by Django 3.2.3 on 2021-07-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notas',
            field=models.TextField(default='notas'),
        ),
    ]
