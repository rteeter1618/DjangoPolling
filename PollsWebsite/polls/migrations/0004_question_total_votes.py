# Generated by Django 4.2.4 on 2023-08-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_choice_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]