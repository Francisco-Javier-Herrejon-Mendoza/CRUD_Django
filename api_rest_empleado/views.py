from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from crud.models import Empleado
from .serializers import EmpleadoSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def get_post_empleado(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        datos = JSONParser().parse(request)
        serializer = EmpleadoSerializer(data = datos)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def put_delete_empleado(request,id):
    try:
        empleado = Empleado.objects.get(idEmpleado = id)
    except Empleado.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)
    elif request.method == 'PUT':
        datos = JSONParser().parse(request)
        serializer = EmpleadoSerializer(empleado, data = datos)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        empleado.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)