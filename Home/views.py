from django.shortcuts import render,redirect
from Home.models import Stadium
from Home.serializers import StadiumSerializer,TeamSerializer
from config import secrets
import json

def user_home(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    stadiums=Stadium.objects.all()
    geoData=[]
    for stadium in stadiums:
        data={
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [stadium.longitude, stadium.latitude]
            },
            "properties": {
                "title": stadium.name,
                "address": stadium.city,
                "description": stadium.image,
                "water": True,
                "outdoor": False,
                "civil": False,
                "wildlife": True,
                "heritage": False,
                "marker-color": "#94a748"
            }
        }
        geoData.append(json.dumps(data))
    context={
        "stadiums":geoData,
        "secretToken":secrets.MAPBOX_SECRETS,
        }
    return render(request,"home.html",context)