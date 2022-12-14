# Generated by Django 4.1 on 2022-08-23 15:38

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Category"s',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Product', verbose_name='Product Img')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(max_length=15000, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Price')),
                ('Availability', models.BooleanField(default=True, null=True, verbose_name='Availability')),
                ('color', models.CharField(max_length=20, null=True, verbose_name='Color')),
                ('slug', models.SlugField(max_length=100, null=True, verbose_name='Slug')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductCategory', to='product.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-id'],
            },
        ),
    ]
