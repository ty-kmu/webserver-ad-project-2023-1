# Generated by Django 4.2 on 2023-06-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_questionedithistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
    ]
