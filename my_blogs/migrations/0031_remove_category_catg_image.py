# Generated by Django 4.1.2 on 2022-11-04 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0030_alter_category_catg_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catg_image',
        ),
    ]
