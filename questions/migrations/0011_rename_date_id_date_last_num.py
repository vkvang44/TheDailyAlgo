# Generated by Django 4.0.2 on 2022-03-05 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_date_date_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='date_id',
            new_name='last_num',
        ),
    ]