# Generated by Django 5.0.3 on 2024-03-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
