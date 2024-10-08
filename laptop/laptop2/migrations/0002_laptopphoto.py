# Generated by Django 5.1.1 on 2024-09-15 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='laptop_photos/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='laptop2.laptop')),
            ],
        ),
    ]
