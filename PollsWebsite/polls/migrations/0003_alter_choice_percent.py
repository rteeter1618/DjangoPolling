# Generated by Django 4.2.4 on 2023-08-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='percent',
            field=models.FloatField(default=0),
        ),
    ]