# Generated by Django 5.1.2 on 2024-12-21 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='reviews',
        ),
    ]
