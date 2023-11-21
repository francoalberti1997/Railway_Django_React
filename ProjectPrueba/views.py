<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from prueba_api import models

def index(request):
    persona = models.Persona.objects.all()
    return render("index.html")
=======
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")
>>>>>>> master
