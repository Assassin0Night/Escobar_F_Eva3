from django.shortcuts import render,redirect
from .serializer import inscripcionSerial, institucionSerial
from .models import Inscrito,Institucion
from .forms import InscritoForm,InstitucionForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from django.http.response import JsonResponse
import requests
from django.urls import reverse

# Create your views here.
class inscripcion_list_class(APIView):
    def get(self,request):
        inscrito = Inscrito.objects.all()
        serials = inscripcionSerial(inscrito,many=True)
        return Response(serials.data)
    def post(self,request):
        serials = inscripcionSerial(data = request.data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data,status=status.HTTP_201_CREATED)
        return Response(serials.errors,status=status.HTTP_400_BAD_REQUEST)

class inscripcion_class(APIView):
    def get_object(self,pk):
        try:
            inscrit = Inscrito.objects.get(pk=id)
    
        except:
            return Response(Http404)
    def get(self,request,pk):
        inscrit = self.get_object(pk)
        serial = inscripcionSerial(inscrit)
        return Response(serial.data)
    def put(self, request,pk):
        inscrit = self.get_object(pk)
        serial = inscripcionSerial(inscrit,data=request.data)
        if serial.is_valid:
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        inscrit = self.get_object(pk)
        inscrit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class institucion_list_class(APIView):
    def get(self,request):
        institucion = Institucion.objects.all()
        serials = inscripcionSerial(institucion,many=True)
        return Response(serials.data)
    def post(self,request):
        serials = inscripcionSerial(data = request.data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data,status=status.HTTP_201_CREATED)
        return Response(serials.errors,status=status.HTTP_400_BAD_REQUEST)
    
class institucion_class(APIView):
    def get_object(self,pk):
        try:
            institucion = Institucion.objects.get(pk=id)
    
        except:
            return Response(Http404)
    def get(self,request,pk):
        institucion = self.get_object(pk)
        serial = institucionSerial(institucion)
        return Response(serial.data)
    def put(self, request,pk):
        institucion = self.get_object(pk)
        serial = institucionSerial(institucion,data=request.data)
        if serial.is_valid:
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        institucion = self.get_object(pk)
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def inscripcion_list(request):
    if request.method == 'GET':
        inscrito = Inscrito.objects.all()
        serials = inscripcionSerial(inscrito,many=True)
        return Response(serials.data)

    if request.method == 'POST':
        serials = inscripcionSerial(data = request.data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data, status=status.HTTP_201_CREATED)
        return Response(serials.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def inscripcion_detalle(request,id):
    try:
        inscrito = Inscrito.objects.get(pk=id)
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
   #obtener datos
    if request.method == 'GET':
        serial = inscripcionSerial(inscrito)
        return Response(serial.data)
    
    #poner datos
    if request.method == 'PUT':
        serial = inscripcionSerial(inscrito,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #borrar datos
    if request.method == 'DELETE':
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        institucion = Institucion.objects.all()
        serials = institucionSerial(institucion,many=True)
        return Response(serials.data)

    if request.method == 'POST':
        serials = institucionSerial(data = request.data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data, status=status.HTTP_201_CREATED)
        return Response(serials.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def institucion_detalle(request,id):
    try:
        institucion = Institucion.objects.get(pk=id)
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
   #obtener datos
    if request.method == 'GET':
        serial = institucionSerial(institucion)
        return Response(serial.data)
    
    #poner datos
    if request.method == 'PUT':
        serial = institucionSerial(institucion,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #borrar datos
    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return render(request,'index.html')

def usuario(request):
    data={'nombre':'Francisco',
          'apellido':'Escobar',
          'rut':'21.554.584-9',
          'seccion':'(IEI-170-N4/D)'}
    return JsonResponse(data)


def agregar_instituto(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            # Guarda en la API
            data = form.cleaned_data
            response = requests.post('http://127.0.0.1:8000/institucion/', data=data)
            
            if response.status_code == 201:
                # Si la creación en la API externa fue exitosa, redirige a alguna página de éxito
                return redirect('/')
    else:
        form = InstitucionForm()
        data = {'form': form}
    return render(request, 'agregar.html', data)



def lista_inscrito(request):
    inscrito = Inscrito.objects.all()
    data = {'inscrito' : inscrito}
    return render(request,'inscrito.html',data)



def agregar_inscripcion(request):
    if request.method == 'POST':
        form = InscritoForm(request.POST)
        if form.is_valid():
            # Guarda en la API
            data = form.cleaned_data
            response = requests.post('http://127.0.0.1:8000/inscripciones/', data=data)
            
            if response.status_code == 201:
                # Si la creación en la API externa fue exitosa, redirige a alguna página de éxito
                return redirect('/')
    else:
        form = InscritoForm()
        data = {'form': form}
    return render(request, 'agregar.html', data)