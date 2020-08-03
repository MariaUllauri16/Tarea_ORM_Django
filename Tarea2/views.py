from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def menu(request):
    opciones = {'Menu':'Menu Principal','Contacto':'Contacto del Blog'}
    return render(request,'principal.html',opciones)