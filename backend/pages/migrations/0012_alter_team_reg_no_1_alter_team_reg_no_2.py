# Generated by Django 4.0.4 on 2022-06-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_team_no_of_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='reg_no_1',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='reg_no_2',
            field=models.BigIntegerField(blank=True),
        ),
    ]