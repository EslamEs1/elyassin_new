# Generated by Django 4.1 on 2022-08-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post', verbose_name='image')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.TextField(max_length=15000, verbose_name='text')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('slug', models.SlugField(max_length=200, verbose_name='Dont Touch This')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
