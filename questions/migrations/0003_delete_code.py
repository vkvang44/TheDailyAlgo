# Generated by Django 4.0.2 on 2022-02-23 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Code',
        ),
    ]