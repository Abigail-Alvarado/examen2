from django.db import models


class Ordenes(models .Model):

    id = models.AutoField(primary_key=True)
    nombreCliente = models.CharField(max_length=150)
    total = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)   
 
    
 

    
             