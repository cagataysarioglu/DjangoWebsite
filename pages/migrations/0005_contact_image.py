# Generated by Django 3.1.5 on 2021-01-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210118_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Görsel'),
        ),
    ]
