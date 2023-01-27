from rest_framework import viewsets
from iacrud.api import serializer
from iacrud import models

class IaCrudViewsets(viewsets.ModelViewSet):
    
    serializer_class=serializer.IaCrudSerializer
    
    queryset=models.IaCrud.objects.all()