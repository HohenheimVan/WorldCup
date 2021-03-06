# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 19:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=16)),
                ('team_1_score', models.IntegerField()),
                ('team_2_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=16)),
                ('group', models.CharField(max_length=1)),
                ('pkt', models.IntegerField(default=0)),
                ('matches', models.IntegerField(default=0)),
                ('win', models.IntegerField(default=0)),
                ('loose', models.IntegerField(default=0)),
                ('draw', models.IntegerField(default=0)),
                ('FIFA', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('team_1_score', models.IntegerField()),
                ('team_2_score', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='WCScores.Match')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='team_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_1', to='WCScores.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_2', to='WCScores.Team'),
        ),
    ]
