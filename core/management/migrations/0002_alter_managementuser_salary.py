# Generated by Django 4.1.3 on 2022-11-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managementuser',
            name='salary',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
