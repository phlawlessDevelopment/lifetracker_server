# Generated by Django 4.2.4 on 2023-08-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_sleeprange_moodchoice_digestionchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifetrackmodel',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
