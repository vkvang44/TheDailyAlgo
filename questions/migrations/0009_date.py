# Generated by Django 4.0.2 on 2022-03-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_question_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField()),
            ],
        ),
    ]