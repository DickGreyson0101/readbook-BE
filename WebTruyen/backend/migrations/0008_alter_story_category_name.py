# Generated by Django 4.1.2 on 2022-10-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='category_name',
            field=models.ManyToManyField(blank=True, to='backend.category'),
        ),
    ]
