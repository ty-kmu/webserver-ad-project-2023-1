# Generated by Django 4.2 on 2023-05-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_comment_voter_alter_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
    ]
