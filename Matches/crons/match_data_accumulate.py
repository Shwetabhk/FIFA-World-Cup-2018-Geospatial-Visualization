from django_cron import CronJobBase, Schedule
from Home.models import Team, Stadium, Channel
from FIFA2018.data import Data
from Matches.models import Match
from datetime import datetime
import os
import json


class MatchDataAccumulate(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'Home.matchdata'

    def do(self):
        try:
            data = Data.DATASET
            groups = data['groups']
            matches = []
            for group in groups:
                group_matches = groups[group]['matches']
                for match in group_matches:
                    match["round"] = group
                    matches.append(match)
            knockouts = data['knockout']
            for knockout in knockouts:
                knockout_matches = knockouts[knockout]['matches']
                for match in knockout_matches:
                    match["round"] = knockout
                    matches.append(match)
            for match in matches:
                winner = None
                if(match['home_result'] > match['away_result']):
                    winner = match['home_team']
                elif(match['away_result'] > match['home_result']):
                    winner = match['away_team']
                date = match['date'][0:-3]+match['date'][-2:]
                datetime_object = datetime.strptime(
                    date, "%Y-%m-%dT%H:%M:%S%z")
                match_object, flag = Match.objects.get_or_create(
                    id=match["name"],
                    match_type=match["type"],
                    home_team=self.get_team(match["home_team"]),
                    away_team=self.get_team(match["away_team"]),
                    home_result=match["home_result"],
                    away_result=match["away_result"],
                    date=datetime_object,
                    stadium=self.get_stadium(match['stadium']),
                    # channels = self.get_channels(match['channels']),
                    finished=match['finished'],
                    matchday=match['matchday'],
                    tournament_round=match['round'],
                    winner=self.get_team(winner)
                )
                channels = self.get_channels(match['channels'])
                match_object.channels.add(*channels)
        except Exception as e:
            print(e)

    @staticmethod
    def get_stadium(s_id):
        stadium = Stadium.objects.get(id=s_id)
        return stadium

    @staticmethod
    def get_team(t_id):
        if t_id:
            team = Team.objects.get(id=t_id)
            return team
        return None

    @staticmethod
    def get_channels(c_list):
        channels = []
        for c_id in c_list:
            channel = Channel.objects.get(id=c_id)
            channels.append(channel)
        return channels
