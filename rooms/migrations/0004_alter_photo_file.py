# Generated by Django 5.1.4 on 2024-12-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_photo_room_alter_room_amenities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]
