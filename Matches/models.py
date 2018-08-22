from django.db import models
from Home.models import Stadium, Team, Channel
from django.contrib.auth import get_user_model


class Match(models.Model):
    match_type = models.CharField(max_length=10)
    home_team = models.ForeignKey(
        Team, related_name="home_team", on_delete=models.CASCADE)
    away_team = models.ForeignKey(
        Team, related_name="away_team", on_delete=models.CASCADE)
    home_result = models.IntegerField(null=False)
    away_result = models.IntegerField(null=False)
    winner = models.ForeignKey(
        Team, related_name="winner", null=True, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    channels = models.ManyToManyField(Channel)
    finished = models.BooleanField(null=False, default=True)
    matchday = models.IntegerField(null=False, default=0)
    tournament_round = models.CharField(max_length=10, default="")


User = get_user_model()


class Comment(models.Model):
    user_name = models.CharField(max_length=30, null=True)
    match = models.ForeignKey(Match, null=True)
    info = models.CharField(max_length=180, null=True)
    date = models.DateTimeField(null=False)
