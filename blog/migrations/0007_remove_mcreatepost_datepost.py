# Generated by Django 4.0.2 on 2022-02-14 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_mcreatepost_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcreatepost',
            name='datepost',
        ),
    ]
