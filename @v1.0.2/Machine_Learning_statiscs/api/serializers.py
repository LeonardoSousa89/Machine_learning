from rest_framework import serializers
from Machine_Learning_statiscs import models

class NayveeBasyesSerializers(serializers.ModelSerializer):
    class Meta:
        
        model=models.NayveeBasyes
        
        fields='__all__'
