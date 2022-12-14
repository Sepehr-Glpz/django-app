# Generated by Django 4.1.3 on 2022-11-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntryRequest',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='id')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('resolved', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
