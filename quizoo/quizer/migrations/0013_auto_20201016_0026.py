# Generated by Django 3.1.1 on 2020-10-16 00:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0012_auto_20201011_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
