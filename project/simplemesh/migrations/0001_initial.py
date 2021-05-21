# Generated by Django 2.2.22 on 2021-05-20 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date sent')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplemesh.Conversation')),
            ],
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date sent')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplemesh.Message')),
            ],
        ),
    ]
