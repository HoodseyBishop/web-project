# Generated by Django 2.0.3 on 2018-06-18 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
