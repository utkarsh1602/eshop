# Generated by Django 3.2.4 on 2021-06-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=400),
        ),
    ]
