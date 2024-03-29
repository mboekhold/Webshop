# Generated by Django 2.1.4 on 2019-01-03 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('image', models.ImageField(blank=True, upload_to='profile_pics')),
                ('first_name', models.CharField(default='No First Name', max_length=50)),
                ('last_name', models.CharField(default='No Last Name', max_length=50)),
                ('description', models.TextField(default='No Description')),
                ('quote', models.TextField(default='No Quote')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
