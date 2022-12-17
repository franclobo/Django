from django.http import HttpResponse
import datetime

def saludo(request): # Primera vista
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Adios mundo cruel")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):

    #edadActual = 18

    periodo = agno - 2022
    edadFutura = edad + periodo

    documento = """<html>
    <body>
    <h2>
    En el año %s tendras %s años
    </h2>
    </body>
    </html>""" % (agno, edadFutura)

    return HttpResponse(documento)