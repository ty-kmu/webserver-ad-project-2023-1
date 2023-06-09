# Generated by Django 4.2 on 2023-05-29 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_comment_modify_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionEditHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('previous_subject', models.CharField(max_length=200)),
                ('previous_content', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.question')),
            ],
        ),
    ]
