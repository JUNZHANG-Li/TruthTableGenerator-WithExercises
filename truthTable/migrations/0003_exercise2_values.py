# Generated by Django 2.1.5 on 2022-03-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truthTable', '0002_exercise2_generator'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise2',
            name='values',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
