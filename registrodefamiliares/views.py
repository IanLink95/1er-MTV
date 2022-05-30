from django.http import HttpResponse
from django.shortcuts import render
from registrodefamiliares.models import Familiar,Nacionalidad

def familiar1 (self):
    familiar1= Familiar(id_familiar= 1,nombre='Alejandro',apellido='Gonzalez',dni=13456789,fecha_nacimiento='1958-12-02',direccion='Av. Rivadavia 9889 12 C',telefono="+541172728999",numero_nacionalidad=3,vive=True)
    familiar1.save()
    documento= f"Nombre: {familiar1.nombre}"
    return HttpResponse(documento)


def familiar2 (self):
    familiar2= Familiar (id_familiar= 2,nombre='Alexis',apellido='Gonzalez',dni=34456678,fecha_nacimiento='1998-10-21',direccion='Paysandu 789 2 D',telefono="+541545755878",numero_nacionalidad= 1,vive=True)
    familiar2.save()
    documento= f"Nombre: {familiar2.nombre}"
    return HttpResponse(documento)

def familiar3(self):
    familiar3= Familiar(id_familiar= 3,nombre="Maria Marta",apellido="Perez",dni=12445679,fecha_nacimiento='1960-12-04',direccion="Av. Rivadavia 9889 12 C",telefono="+541548717657",numero_nacionalidad=2,vive=True)
    familiar3.save()
    documento= f"Nombre: {familiar3.nombre}"
    return HttpResponse(documento)

def familiar4(self):
    familiar4= Familiar(id_familiar= 4,nombre="Baltazar",apellido="Gonzalez",dni=29344123,fecha_nacimiento='1978-08-09',direccion="Av. Brasil 889 1 A",telefono="+541564476789",numero_nacionalidad=1,vive=False)
    familiar4.save()
    documento= f"Nombre: {familiar4.nombre}"
    return HttpResponse(documento)

def nacionalidad1(self):
    nacionalidad1= Nacionalidad(numero_nacionalidad=1,descripcion="Argentina")
    nacionalidad1.save()
    documento= f"Nacionalidad: {nacionalidad1.descripcion}"
    return HttpResponse(documento)

def nacionalidad2(self):
    nacionalidad2= Nacionalidad(numero_nacionalidad=2,descripcion="Uruguaya")
    nacionalidad2.save()
    documento= f"Nacionalidad: {nacionalidad2.descripcion}"
    return HttpResponse(documento)

def nacionalidad3(self):
    nacionalidad3= Nacionalidad(numero_nacionalidad=3,descripcion="Brasilera")
    nacionalidad3.save()
    documento= f"Nacionalidad: {nacionalidad3.descripcion}"
    return HttpResponse(documento)

def familiares(request):
    familiares_list= Familiar.objects.all()
    return render(request,'template1.html',{"familiares":familiares_list})