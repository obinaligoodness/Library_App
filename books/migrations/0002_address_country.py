# Generated by Django 4.2.3 on 2023-07-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(default='Nigeria', max_length=50),
        ),
    ]
