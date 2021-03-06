# Generated by Django 3.1.5 on 2021-01-27 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.IntegerField(verbose_name='Kategori Nu.')),
                ('name', models.CharField(max_length=70, verbose_name='Kategori Adı')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Kategori Açıklaması')),
                ('slug', models.SlugField(verbose_name='Bulunak')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ürün Adı')),
                ('amount', models.CharField(max_length=50, verbose_name='Ürün Adedi')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Ürün Fiyatı')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ürün Görseli')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Ürün Açıklaması')),
                ('details', models.TextField(blank=True, null=True, verbose_name='Ürün Detayı')),
                ('slug', models.SlugField(blank=True, verbose_name='Bulunak')),
                ('is_published', models.BooleanField(default=True, verbose_name='Yayında mı?')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Kategori')),
            ],
        ),
    ]
