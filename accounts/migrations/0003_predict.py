# Generated by Django 2.0.13 on 2023-09-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230821_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.FloatField()),
                ('second', models.FloatField()),
                ('third', models.FloatField()),
                ('fourth', models.FloatField()),
            ],
        ),
    ]
