# Generated by Django 5.1.4 on 2024-12-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='two_factor_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
