# Generated by Django 4.1.2 on 2022-10-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0028_alter_comment_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catg_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/category/'),
        ),
    ]
