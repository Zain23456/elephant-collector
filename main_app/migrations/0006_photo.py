# Generated by Django 4.1.3 on 2022-11-09 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_elephant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('elephant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.elephant')),
            ],
        ),
    ]
