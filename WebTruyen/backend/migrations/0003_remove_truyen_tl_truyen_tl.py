# Generated by Django 4.1.2 on 2022-10-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_user_address_user_hobbies_user_intro_user_nickname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truyen',
            name='tl',
        ),
        migrations.AddField(
            model_name='truyen',
            name='tl',
            field=models.ManyToManyField(blank=True, null=True, to='backend.theloai'),
        ),
    ]