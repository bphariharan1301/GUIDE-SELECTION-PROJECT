# Generated by Django 4.0.4 on 2022-06-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_team_reg_no_1_alter_team_reg_no_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='reg_no_2',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='student_2_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='student_2_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='student_2_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]