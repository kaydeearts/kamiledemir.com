# Generated by Django 3.0.3 on 2020-06-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0011_auto_20200627_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_post',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
