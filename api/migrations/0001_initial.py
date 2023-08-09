# Generated by Django 4.2.4 on 2023-08-09 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifetrackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=256)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Digestion',
            fields=[
                ('lifetrackmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.lifetrackmodel')),
            ],
            bases=('api.lifetrackmodel',),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('lifetrackmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.lifetrackmodel')),
                ('meal', models.CharField(max_length=256)),
            ],
            bases=('api.lifetrackmodel',),
        ),
        migrations.CreateModel(
            name='Hydration',
            fields=[
                ('lifetrackmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.lifetrackmodel')),
                ('drink', models.CharField(max_length=256)),
                ('mesurement', models.CharField(max_length=256)),
                ('amount', models.PositiveSmallIntegerField()),
            ],
            bases=('api.lifetrackmodel',),
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('lifetrackmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.lifetrackmodel')),
            ],
            bases=('api.lifetrackmodel',),
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('lifetrackmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.lifetrackmodel')),
            ],
            bases=('api.lifetrackmodel',),
        ),
        migrations.CreateModel(
            name='Smoking',
            fields=[
                ('lifetrackmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.lifetrackmodel')),
                ('count', models.PositiveSmallIntegerField()),
                ('weight', models.FloatField()),
            ],
            bases=('api.lifetrackmodel',),
        ),
    ]