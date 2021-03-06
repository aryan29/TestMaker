# Generated by Django 3.1.1 on 2020-10-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0008_quiz_record_responses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='resume_late',
            new_name='resume_later',
        ),
        migrations.AddField(
            model_name='quiz',
            name='reveal_answers_after_test',
            field=models.BooleanField(default=False),
        ),
    ]
