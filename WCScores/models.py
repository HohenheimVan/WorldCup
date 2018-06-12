from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Team(models.Model):
    country = models.CharField(max_length=16, unique=True)
    group = models.CharField(max_length=1)
    pkt = models.IntegerField(default=0)
    matches = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    loose = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    FIFA =models.IntegerField(unique=True)
    def __str__(self):
        return self.country

class Match(models.Model):
    datetime = models.DateTimeField()
    day = models.CharField(max_length=16, null=True, blank=True)
    team_1 = models.ForeignKey(Team, related_name= 'team_1', )
    team_2 = models.ForeignKey(Team, related_name='team_2')
    team_1_score = models.IntegerField(null=True, blank=True)
    team_2_score = models.IntegerField(null=True, blank=True)
    winner = models.ForeignKey(Team, related_name='winner', null=True, blank=True)
    draw = models.BooleanField(default=False)

class UserScore(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    name = models.ForeignKey(User, related_name='name')
    team_1_score = models.IntegerField()
    team_2_score = models.IntegerField()
    match = models.ForeignKey(Match, related_name='match')
    scored = models.BooleanField(default=False)
    perfect = models.BooleanField(default=False)


class Scoreboard(models.Model):
    user = models.ForeignKey(User, related_name= 'user')
    matches_number = models.IntegerField(default=0)
    scored = models.IntegerField(default=0)
    perfect = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
