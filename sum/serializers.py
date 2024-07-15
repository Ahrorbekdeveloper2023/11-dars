from rest_framework import serializers

from .models import DailyCost

class DailyCostSerializer(serializers.ModelSerializer):
    class Meta:
        models = DailyCost
        fields = '__all__'