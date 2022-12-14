# Generated by Django 4.1 on 2022-08-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_are_we', models.TextField(blank=True, max_length=150000, null=True, verbose_name='About Us')),
            ],
            options={
                'verbose_name': 'About us',
                'verbose_name_plural': 'About us',
            },
        ),
        migrations.CreateModel(
            name='Our_Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('service_description', models.TextField(blank=True, max_length=150000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Our Service',
                'verbose_name_plural': 'Our Services',
            },
        ),
        migrations.CreateModel(
            name='Img_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_img', models.ImageField(upload_to='service_img', verbose_name='Image')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Service', to='about.our_services', verbose_name='Service')),
            ],
            options={
                'verbose_name': 'Image service',
                'verbose_name_plural': 'Image service',
            },
        ),
    ]
