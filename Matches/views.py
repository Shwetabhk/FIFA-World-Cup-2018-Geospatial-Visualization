from django.shortcuts import render, redirect
from Matches.models import Match
from Home.models import Stadium
from config import secrets
import json


def matches(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    matches = Match.objects.all()
    geoData = []
    for match in matches:
        if not match.winner:
            winner = "Draw"
        else:
            winner = match.winner.name
        data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [match.stadium.longitude, match.stadium.latitude]
            },
            "properties": {
                "name": match.id,
                "type": match.match_type,
                "home_team": match.home_team.name,
                "away_team": match.away_team.name,
                "home_result": match.home_result,
                "away_result": match.away_result,
                "date": str(match.date),
                "stadium": match.stadium.name,
                "channels": [[channel.name, channel.icon] for channel in match.channels.all()],
                "finished": True,
                "matchday": match.matchday,
                "round": match.tournament_round,
                "winner": winner,
                "home_flag":match.home_team.flag,
                "away_flag":match.away_team.flag,
                "marker-color": "#94a748"
            }
        }
        geoData.append(json.dumps(data))
    return render(request, "matches.html", {"matches": geoData, "secretToken": secrets.MAPBOX_SECRETS})
