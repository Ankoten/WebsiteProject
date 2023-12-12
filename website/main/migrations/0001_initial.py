# Generated by Django 4.2.6 on 2023-12-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advert', models.CharField(max_length=100)),
                ('price', models.PositiveBigIntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('rooms', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('payment_hcs', models.BooleanField(default=False)),
                ('deposit', models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_name', max_length=255)),
                ('image', models.ImageField(default='default_image.jpg', upload_to='images/')),
                ('advert', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.advertmodel')),
            ],
        ),
        migrations.AddField(
            model_name='advertmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usermodel'),
        ),
    ]