# Generated by Django 4.1.2 on 2022-10-16 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0013_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic',
        ),
    ]