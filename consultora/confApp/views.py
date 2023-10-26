from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from django.shortcuts import render

def visual(request):
    return render(request, 'base.html')
   

    
def mostrar_datos_json(request):
    with open('confApp/Datos-ONIET---Hoja-1---JSON.json', 'r') as json_file:
        data = json.load(json_file)
    json_file.close()

    produccionesTotales = [0,0,0,0,0]
    CantidaPiezasConFallas= [0,0,0,0,0]
    CantPiezasOk = [0,0,0,0,0]
    PiezasOk = [0,0,0,0,0]
    PiezasError = [0,0,0,0,0]
    # empresa = {
    #     produccionesTotales = [0,0,0,0,0]
    #     CantidaPiezasConFallas= [0,0,0,0,0]
    #     CantPiezasOk = [0,0,0,0,0]
    #     PiezasOk = [0,0,0,0,0]
    #     PiezasError = [0,0,0,0,0]
    # }
    for i in range(5):
        for empresa in data:
            if empresa["Empresa"] == "Empresa 1":
                produccionesTotales[0]+= empresa["ProduccionTotal"]
                CantidaPiezasConFallas[0] += empresa["CantidaPiezasConFallas"]
            elif empresa["Empresa"] == "Empresa 2":
                produccionesTotales[1]+= empresa["ProduccionTotal"]
                CantidaPiezasConFallas[1] += empresa["CantidaPiezasConFallas"]
            elif empresa["Empresa"] == "Empresa 3":
                produccionesTotales[2]+= empresa["ProduccionTotal"]
                CantidaPiezasConFallas[2] += empresa["CantidaPiezasConFallas"]
            elif empresa["Empresa"] == "Empresa 4":
                produccionesTotales[3]+= empresa["ProduccionTotal"]
                CantidaPiezasConFallas[3] += empresa["CantidaPiezasConFallas"]
            elif empresa["Empresa"] == "Empresa 5":
                produccionesTotales[4]+= empresa["ProduccionTotal"]
                CantidaPiezasConFallas[4] += empresa["CantidaPiezasConFallas"]
        print(produccionesTotales)
        print(CantidaPiezasConFallas)
    resultados = []
    for i in range(5):
        empresa = {}
        empresa['productosTotales'] = produccionesTotales[i]
        empresa['productosFallidos'] = CantidaPiezasConFallas[i]
        empresa['cantPiezasOk'] = (produccionesTotales[i] - CantidaPiezasConFallas[i])

        CantPiezasOk[i] = (produccionesTotales[i] - CantidaPiezasConFallas[i])
        PiezasOk[i] = CantPiezasOk[i] - produccionesTotales[i]

        resultados.append(empresa)

    return render(request,'base.html', {
        'datos': data,
        'empresa': empresa,
        'resultados': resultados
        })


#CantPiezasOk = ProduccionTotal - CantidaPiezasConFallas
#%PiezasOk = CantPiezasOk / ProduccionTotal
#%PiezasError = CantidaPiezasConFallas / ProduccionTotal

"""

totales = []
    for i in range(5):
        empresacomp = empresa[1]["Empresa"]
        print(empresacomp)
        for empresa in data:
            
            for i in range(len(data)):
                if empresa["Empresa"] == (empresacomp):
                    totalProduccion += int(empresa["ProduccionTotal"])  
            totales.append(totalProduccion)

"""