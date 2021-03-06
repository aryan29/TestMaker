# Generated by Django 3.1.1 on 2020-10-11 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0010_quiz_expired'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordedResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_num', models.SmallIntegerField()),
                ('reponses', models.CharField(max_length=2000)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizer.usersgivingtest')),
            ],
        ),
    ]
