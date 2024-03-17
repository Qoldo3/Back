# Generated by Django 4.2.6 on 2023-12-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('context', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('abstract', models.TextField()),
            ],
        ),
    ]