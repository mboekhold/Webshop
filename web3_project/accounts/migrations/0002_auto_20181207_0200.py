# Generated by Django 2.1.3 on 2018-12-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default='No Description', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='No First Name', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='No Last Name', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='quote',
            field=models.CharField(default='No Quote', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
