from rest_framework import serializers
from . import models


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vessel
        fields = ['code', 'name', 'created']


class MovementHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovementHistory
        fields = ['longitude', 'latitude', 'movement_datetime', 'created']
