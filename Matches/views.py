from django.shortcuts import render, redirect
from django.http import JsonResponse
from Matches.models import Match, Comment
from Home.models import Stadium
from Matches.serializers import CommentSerializer
from config import secrets
from datetime import datetime
from Matches.forms import CommentForm
import json


def matches(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect("/login")
        form = CommentForm(request.POST or None)
        matches = Match.objects.all()
        geoData = []
        for match in matches:
            comments = Comment.objects.filter(match_id=match).all()
            comments = json.dumps(CommentSerializer(comments, many=True).data)
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
                    "home_flag": match.home_team.flag,
                    "away_flag": match.away_team.flag,
                    "marker-color": "#94a748",
                    "comments": comments
                }
            }
            geoData.append(json.dumps(data))
        return render(request, "matches.html", {"matches": geoData, "secretToken": secrets.MAPBOX_SECRETS, "form": form})
    elif request.method == "POST":
        form = CommentForm(request.POST or None)
        match = int(request.POST.get('match'))
        print(match)
        match_obj = Match.objects.get(id=match)
        if form.is_valid():
            comment = form.cleaned_data.get("comment")
            comment_obj = Comment.objects.create(
                user_name=request.user.username,
                match_id=match,
                info=comment,
                date=datetime.now()
            )
            result = CommentSerializer(comment_obj)
        return JsonResponse(result.data, safe=False)


def comments(request):
    if request.method == "GET":
        match = int(request.GET['match'])
        match = Match.objects.get(id=match)
        comments = Comment.objects.filter(match_id=match).all()
        comments = CommentSerializer(comments, many=True).data
        print(comments)
        return JsonResponse(comments,safe=False)
