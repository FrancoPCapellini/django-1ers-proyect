from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader



from django.template import Context

def saludo(request):
    return HttpResponse("hola Django - Coder")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentodetexto = f"Mi nombre es: {nombre}"
    return HttpResponse(documentodetexto)

def MiPrimeraPlantilla(request):
    # Abrimos el documento que tiene la plantilla:
    plantiallaExterna = open("myproject/templates/plantilla1.html")
    # Cargar el documento en una variable de tipo "Template":
    template = Template(plantiallaExterna.read())
    # Cerrar el documento externo que abrimos:
    plantiallaExterna.close()
    # Crear un contexto:
    contexto = Context() #es un objeto que nos permite indicar que atributos, variables o funciones va a usar la plantilla (Contenedor para poder pasarle parametros)
    # Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def probando_template(request):
    nombre = "Franco"
    apellido = "Peña"
    lista_de_notas = [8,2,3,9,10]
    diccionario = {"nombre":nombre,
                   "apellido":apellido,
                   "hoy":datetime.datetime.now(),
                   "notas":lista_de_notas
                   } 
    plantilla = loader.get_template("plantilla1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)  