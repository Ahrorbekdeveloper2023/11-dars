from django.shortcuts import render

from .models import DailyCost
from .serializers import DailyCostSerializer
from .permissions import DailyCostPermissions

from rest_framework.viewsets import ModelViewSet

class DailyCostModelViewSet(ModelViewSet):
    queryset = DailyCost.objects.all()
    serializer_class = DailyCostSerializer
    permission_classes = [DailyCostPermissions]
