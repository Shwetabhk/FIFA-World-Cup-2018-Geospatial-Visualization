from django.shortcuts import render, redirect
from Home.models import Stadium, Channel, Team
from config import secrets
import json


def home(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "home.html", {})


def teams(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    teams = Team.objects.all()
    geoData = []
    for team in teams:
        data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [team.longitude, team.latitude]
            },
            "properties": {
                "title": team.name,
                "address": team.flag,
                "description": team.fifacode,
                "marker-color": "#94a748"
            }
        }
        geoData.append(json.dumps(data))
    return render(request, "teams.html", {"teams": geoData, "secretToken": secrets.MAPBOX_SECRETS})


def stadiums(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    stadiums = Stadium.objects.all()
    geoData = []
    for stadium in stadiums:
        data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [stadium.longitude, stadium.latitude]
            },
            "properties": {
                "title": stadium.name,
                "address": stadium.city,
                "description": stadium.image,
                "marker-color": "#94a748"
            }
        }
        geoData.append(json.dumps(data))
    return render(request, "stadiums.html", {"stadiums": geoData, "secretToken": secrets.MAPBOX_SECRETS})


def tv_channels(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    channels = Channel.objects.all()
    geoData = []
    for channel in channels:
        data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [channel.longitude, channel.latitude]
            },
            "properties": {
                "title": channel.name,
                "address": channel.country,
                "language": channel.language,
                "description": channel.icon,
                "marker-color": "#94a748"
            }
        }
        geoData.append(json.dumps(data))
    return render(request, "channels.html", {"channels": geoData, "secretToken": secrets.MAPBOX_SECRETS})
