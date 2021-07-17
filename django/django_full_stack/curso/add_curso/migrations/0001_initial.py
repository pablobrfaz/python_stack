# Generated by Django 3.2.3 on 2021-07-17 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='description',
            fields=[
                ('curso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='add_curso.curso')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
