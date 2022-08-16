from .models import Games
from rest_framework import serializers

class GamesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields =['id','name', 'description', 'year']