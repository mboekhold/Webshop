# Generated by Django 2.1.3 on 2018-12-02 13:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20181202_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='userCart',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
