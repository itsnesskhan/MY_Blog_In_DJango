# Generated by Django 3.1.2 on 2021-06-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='F:\\My Videos\\images\\default.jpg', upload_to='images'),
        ),
    ]
