# Generated by Django 3.0.8 on 2020-07-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200704_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='blog', width_field='width_field'),
        ),
    ]
