from django_cron import CronJobBase, Schedule
from Home.models import Channel
from FIFA2018.data import Data
from Home.util.country_coordinates import CountryCoordinates
from Home.util.lang_iso import LangIso
import os
import json


class ChannelDataAccumulate(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'Home.channeldata'

    def do(self):
        data = Data.DATASET
        tvchannels = data['tvchannels']
        codes = LangIso.ISO639_2
        try:
            for tvchannel in tvchannels:
                coordinates = CountryCoordinates.getCoordinates(
                    tvchannel["country"])
                lang = tvchannel['lang'][0]
                tv_object, flag = Channel.objects.get_or_create(
                    id=tvchannel['id'],
                    name=tvchannel['name'],
                    country=tvchannel['country'],
                    language=codes[lang],
                    latitude=coordinates[0],
                    longitude=coordinates[1],
                    icon=tvchannel['icon']
                )
        except Exception as e:
            print(e)
