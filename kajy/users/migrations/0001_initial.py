# Generated by Django 3.0.8 on 2020-08-23 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='users/avatar/default.jpg', upload_to=users.models.re_name)),
                ('dateNaissance', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('adresse', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
