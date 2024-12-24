# Generated by Django 5.1.4 on 2024-12-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('cleanliness', models.IntegerField()),
                ('accuracy', models.IntegerField()),
                ('check_in', models.IntegerField()),
                ('communication', models.IntegerField()),
                ('location', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
