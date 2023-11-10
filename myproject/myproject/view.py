from django.http import HttpResponse
import datetime
from django.template import Template, Context



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

def probando_template(request):
    nombre = "Franco"
    apellido = "Peña"
    
    diccionario = {"nombre":nombre, "apellido":apellido} # <------ Para enviar al contexto
    
    mi_html = open("myproject/templates/plantilla1.html","r")
    
    plantilla = Template(mi_html.read())
    
    mi_html.close()
    
    mi_contexto = Context(diccionario)
    
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)

def MiPrimeraPlantilla(request):
    # Abrimos el documento que tiene la plantilla:
    plantiallaExterna = open("myproject/templates/plantilla1.html","r")
    # Cargar el documento en una variable de tipo "Template":
    template = Template(plantiallaExterna.read())
    # Cerrar el documento externo que abrimos:
    plantiallaExterna.close()
    # Crear un contexto:
    contexto = Context() #es un objeto que nos permite indicar que atributos, variables o funciones va a usar la plantilla (Contenedor para poder pasarle parametros)
    # Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)
    