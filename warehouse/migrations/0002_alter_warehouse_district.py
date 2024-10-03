# Generated by Django 4.2 on 2024-09-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='district',
            field=models.CharField(choices=[('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sai Kung', 'Sai Kung'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Yuen Long', 'Yuen Long'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Sham Shui Po', 'Sham Shui Po'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'), ('Central & Western', 'Central & Western'), ('Eastern', 'Eastern'), ('Southern', 'Southern'), ('Wan Chai', 'Wan Chai')], max_length=50),
        ),
    ]
