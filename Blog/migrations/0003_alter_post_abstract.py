# Generated by Django 4.2.6 on 2023-12-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_remove_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.TextField(max_length=350),
        ),
    ]