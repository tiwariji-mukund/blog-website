# Generated by Django 4.1.2 on 2022-10-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0003_post_delete_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='MyBlogs', max_length=200),
        ),
    ]
