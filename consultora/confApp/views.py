from django.shortcuts import render
from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from django.shortcuts import render

def visual(request):
    return render(request, 'base.html')

    
def mostrar_datos_json(request):
    with open('confApp/Datos-ONIET---Hoja-1---JSON.json', 'r') as json_file:
        data = json.load(json_file)

    return render('jsondata.html', 'dast')
