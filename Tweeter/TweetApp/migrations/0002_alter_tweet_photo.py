# Generated by Django 5.0.8 on 2024-08-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TweetApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
