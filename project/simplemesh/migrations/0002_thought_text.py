# Generated by Django 2.2.22 on 2021-05-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplemesh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='text',
            field=models.CharField(default='Default thought message', max_length=200),
            preserve_default=False,
        ),
    ]
