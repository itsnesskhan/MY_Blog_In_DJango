# Generated by Django 3.1.2 on 2021-06-28 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_auto_20210628_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images'),
        ),
    ]
