# Generated by Django 4.0.4 on 2022-06-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_remove_team_guide_team_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=100)),
                ('otp', models.CharField(max_length=10)),
            ],
        ),
    ]
