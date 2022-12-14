# Generated by Django 4.1.3 on 2022-11-27 07:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryrequest',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='entryrequest',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
