# Generated by Django 2.2.24 on 2021-11-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maillog', '0002_auto_20200916_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillog',
            name='date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
