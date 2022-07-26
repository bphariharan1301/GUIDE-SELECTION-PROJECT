# Generated by Django 4.0.4 on 2022-07-06 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_remove_temp_team_guide_remove_temp_team_reg_no_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_team',
            name='guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.guide'),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='reg_no_2',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='reg_no_3',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_2_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_2_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_2_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_3_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_3_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='temp_team',
            name='student_3_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]