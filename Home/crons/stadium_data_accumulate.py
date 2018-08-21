from django_cron import CronJobBase, Schedule
from Home.models import Stadium
from FIFA2018.data import Data
import os
import json

class StadiumDataAccumulate(CronJobBase):
    RUN_EVERY_MINS = 1 

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code='Home.data' 

    def do(self):
        data = Data.DATASET
        stadiums=data['stadiums']
        try:
            for stadium in stadiums:
                stadium_object,flag=Stadiums.objects.get_or_create(
                    id=stadium['id'],
                    name=stadium['name'],
                    city=stadium['city'],
                    latitude=stadium['lat'],
                    longitude=stadium['lng'],
                    image=stadium['image']
                )
        except Exception as e:
            print(e)
