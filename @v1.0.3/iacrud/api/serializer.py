from rest_framework import serializers
from iacrud import models

class IaCrudSerializer(serializers.ModelSerializer):
    class Meta:
        
        model=models.IaCrud
        fields='__all__'