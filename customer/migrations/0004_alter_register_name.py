# Generated by Django 3.2.6 on 2021-08-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
