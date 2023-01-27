from django.db import models
from uuid import uuid4

class NayveeBasyes(models.Model):

    id_base_de_dado=models.UUIDField(primary_key=True, default=uuid4, editable=False)
    historia=models.CharField(max_length=250)
    divida=models.CharField(max_length=250)
    garantias=models.CharField(max_length=250)
    renda=models.DecimalField(max_digits=10, decimal_places=3)
    
    