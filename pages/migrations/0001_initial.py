# Generated by Django 3.1.5 on 2021-01-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Görsel Adı')),
                ('photo', models.ImageField(null=True, upload_to='', verbose_name='Fotoğraf')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namesurname', models.CharField(max_length=30, verbose_name='Ad-Soyad')),
                ('email', models.EmailField(max_length=254, verbose_name='e-Posta')),
                ('subject', models.CharField(max_length=70, verbose_name='Konu')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/uploads/', verbose_name='Görsel')),
                ('message', models.TextField(verbose_name='İleti')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
            ],
        ),
    ]
