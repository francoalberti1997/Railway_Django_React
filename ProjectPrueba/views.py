from django.shortcuts import render
from django.http import HttpResponse
from prueba_api import models

def index(request):
    persona = models.Persona.objects.all()
    
    return HttpResponse(persona)