# Generated by Django 4.0.2 on 2022-03-08 23:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_alter_constraint_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='example',
            name='question',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='constraint',
            field=ckeditor.fields.RichTextField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='example',
            field=ckeditor.fields.RichTextField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='test_file',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='testcase',
            field=ckeditor.fields.RichTextField(default='1'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Constraint',
        ),
        migrations.DeleteModel(
            name='Example',
        ),
        migrations.DeleteModel(
            name='Testcase',
        ),
    ]