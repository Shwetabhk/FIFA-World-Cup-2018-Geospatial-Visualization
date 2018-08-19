from rest_framework import serializers
from Home.models import Stadium,Team

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stadium
        fields=("__all__")

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=("__all__")
