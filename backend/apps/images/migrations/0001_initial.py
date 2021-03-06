# Generated by Django 3.2.4 on 2021-10-25 22:15

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=50, verbose_name='Name')),
                ('description', models.CharField(db_index=True, default='Anonymous', max_length=500, verbose_name='Description')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated Datetime')),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
            options={
                'db_table': 'Images',
            },
        ),
    ]
