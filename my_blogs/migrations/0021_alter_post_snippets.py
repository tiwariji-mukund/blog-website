# Generated by Django 4.1.2 on 2022-10-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0020_alter_comment_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippets',
            field=models.CharField(max_length=50),
        ),
    ]
