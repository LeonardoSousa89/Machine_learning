from rest_framework import viewsets
from Machine_Learning_statiscs.api import serializers
from Machine_Learning_statiscs import models

class NayveeBasyesViewset(viewsets.ModelViewSet):
    
    serializer_class=serializers.NayveeBasyesSerializers
    
    queryset=models.NayveeBasyes.objects.all()