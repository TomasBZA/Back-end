
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from .forms import InscritoForm, InstitucionForm
from rest_framework.views import APIView
# Create your views here.


def index(request):
    return render(request, 'index.html')


def lista_inscritos(request):
    inscritos = Inscrito.objects.all()
    return render(request, 'lista_inscritos.html', {'inscritos': inscritos})

def inscripcion(request):
    if request.method == 'POST':
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista_inscritos')
    else:
        form = InscritoForm()
    return render(request, 'inscripcion.html', {'form': form})

def eliminar_inscrito(request, id):
    inscrito = Inscrito.objects.get(id=id)
    inscrito.delete()
    return redirect('/lista_inscritos')

def modificar_inscrito(request, id):
    inscrito = Inscrito.objects.get(id=id)
    form = InscritoForm(instance=inscrito)

    if request.method == "POST":
        form = InscritoForm(request.POST, instance=inscrito)
        if (form.is_valid()):
            form.save()
        return redirect('/lista_inscritos')
        
    data = {'form': form}
    return render(request, 'inscripcion.html',data)


def nueva_institucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista_instituciones')
    else:
        form = InstitucionForm()
    return render(request, 'nueva_institucion.html', {'form': form})

def lista_instituciones(request):
    instituciones = Institucion.objects.all()
    return render(request, 'lista_instituciones.html', {'instituciones': instituciones})

def eliminar_institucion(request, id):
    institucion = Institucion.objects.get(id=id)
    institucion.delete()
    return redirect('/lista_instituciones')

def modificar_institucion(request, id):
    institucion = Institucion.objects.get(id=id)
    form = InstitucionForm(instance=institucion)

    if request.method == "POST":
        form = InstitucionForm(request.POST, instance=institucion)
        if (form.is_valid()):
            form.save()
        return redirect('/lista_instituciones')
        
    data = {'form': form}
    return render(request, 'nueva_institucion.html',data)


def datos(request):
    data = {"Nombre": "Tomas Zurita", "Correo": "tomas.zurita02@inacapmail.cl","Celular":"9 3588 0361"}
    return JsonResponse(data)


#class based views
class InscritoListCreate(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


#functions based views
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET'])
def institucion_detail(request, id):
    try:
        institucion = Institucion.objects.get(id=id)
    except Institucion.DoesNotExist:
        return Response(status=404)
    serializer = InstitucionSerializer(institucion)
    return Response(serializer.data)
