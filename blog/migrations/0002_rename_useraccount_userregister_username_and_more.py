# Generated by Django 4.1.dev20211207123650 on 2022-01-26 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregister',
            old_name='useraccount',
            new_name='username',
        ),
        migrations.AddField(
            model_name='userregister',
            name='password1',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
