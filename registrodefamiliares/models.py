from django.db import models
    
class Familiar(models.Model):
    id_familiar=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    fecha_nacimiento=models.DateField()
    direccion=models.CharField(max_length= 40)
    telefono=models.CharField(max_length=60,null=True)
    vive=models.BooleanField()
    numero_nacionalidad= models.IntegerField(null=True)

class Nacionalidad(models.Model):
    numero_nacionalidad= models.IntegerField()
    descripcion= models.CharField(max_length=40)