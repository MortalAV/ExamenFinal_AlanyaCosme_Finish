# Generated by Django 4.1 on 2022-08-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.TextField(max_length=12),
        ),
    ]
