# Generated by Django 4.1 on 2022-08-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name')),
                ('job', models.CharField(blank=True, max_length=200, null=True, verbose_name='Job')),
                ('img', models.ImageField(upload_to='team_img', verbose_name='Image')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'Our Team',
                'verbose_name_plural': 'Our Team',
            },
        ),
    ]
