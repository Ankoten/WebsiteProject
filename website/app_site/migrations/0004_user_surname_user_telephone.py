# Generated by Django 4.2.6 on 2023-12-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site', '0003_remove_user_name_remove_user_surname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Телефон'),
        ),
    ]
