# Generated by Django 5.0.3 on 2024-03-31 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_db', '0003_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(max_length=6),
        ),
    ]
