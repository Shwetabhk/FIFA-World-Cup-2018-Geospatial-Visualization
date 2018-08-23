from django_cron import CronJobBase, Schedule
from Home.models import Team
from Home.util.country_coordinates import CountryCoordinates
from FIFA2018.data import Data
import os
import json


class TeamDataAccumulate(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'Home.teamdata'

    def do(self):
        try:
            data = Data.DATASET
            teams = data['teams']
            for team in teams:
                try:
                    coordinates = CountryCoordinates.getCoordinates(
                        team['name'])
                except:
                    coordinates = [0, 0]
                teams_object, flag = Team.objects.get_or_create(
                    id=team['id'],
                    name=team['name'],
                    fifacode=team['fifaCode'],
                    iso2=team['iso2'],
                    flag=team['flag'],
                    latitude=coordinates[0],
                    longitude=coordinates[1]
                )
        except Exception as e:
            print(e)
