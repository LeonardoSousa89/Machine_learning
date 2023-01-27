from django.db import models
from uuid import uuid4

class IaCrud(models.Model):
    
    id_base_de_dados=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    historia=models.CharField(max_length=250)
    divida=models.CharField(max_length=250)
    garantia=models.CharField(max_length=250)
    renda=models.DecimalField(max_digits=10, decimal_places=3)