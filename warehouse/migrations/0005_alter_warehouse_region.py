# Generated by Django 4.2 on 2024-09-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_alter_warehouse_ninemonrent_alter_warehouse_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='region',
            field=models.CharField(choices=[('Hong_Kong_Island', 'Hong_Kong_Island'), ('New_Territories', 'New_Territories'), ('Kowloon', 'Kowloon')], max_length=50),
        ),
    ]
