from django_cron import CronJobBase, Schedule
from Home.models import Stadiums
import os
import json

class StadiumDataAccumulate(CronJobBase):
    RUN_EVERY_MINS = 1 

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code='Home.data' 

    def do(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(THIS_FOLDER, 'data.json')
        data=json.load(open(file,'r'))
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
