# Generated by Django 3.0.3 on 2020-06-26 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_auto_20200626_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_post',
            name='subgroup',
        ),
    ]
