import os
import json


class Data:
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(THIS_FOLDER, 'data.json')
    DATASET=json.load(open(file,'r'))