from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("hola Django - Coder")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentodetexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentodetexto)