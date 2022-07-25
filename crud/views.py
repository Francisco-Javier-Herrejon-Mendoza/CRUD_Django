from django.shortcuts import render
from .models import Empleado
from .forms import EmpleadoForms, EmpleadoUpdateForms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import json

bandera = True
empleado_buscado = ''

# Create your views here.

def home(request):
    global bandera
    global empleado_buscado

    if bandera:
        #cargarJSON()
        bandera = False

    if request.method == "POST" and "buscar" in request.POST:
        busqueda = request.POST.get("buscar","")
        if busqueda:
            empleado_buscado = Empleado.objects.filter(
                Q(idEmpleado__icontains = busqueda) |
                Q(nombre__icontains = busqueda) |
                Q(apellido__icontains = busqueda) |
                Q(correo__icontains = busqueda) |
                Q(telefono__icontains = busqueda)
            ).distinct()
            return HttpResponseRedirect("/")
        else:
            empleado_buscado = request.POST.get("buscarVacio")
            return HttpResponseRedirect("/")

    empleados = Empleado.objects.all()

    contexto = {
        'empleados' : empleados,
        'empleado_buscado':empleado_buscado,
        'form' : EmpleadoForms()
    }

    if request.method == 'POST' and "crear" in request.POST:
        data = EmpleadoForms(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect("/")

    if request.method == 'POST' and "editar" in request.POST:
        id = request.POST.get("editar","")
        name = request.POST.get("nombre","")
        last_name = request.POST.get("apellido","")
        mail = request.POST.get("correo","")
        phone = request.POST.get("telefono","")
        Empleado.objects.filter(idEmpleado = id).update(nombre = name, apellido = last_name, correo = mail, telefono = phone)
        return HttpResponseRedirect("/")

    if request.method == 'POST' and "eliminar" in request.POST:
        id = request.POST.get("eliminar","")
        empleado = Empleado.objects.get(idEmpleado = id)
        empleado.delete()
        return HttpResponseRedirect("/")

    return render(request, 'index.html', contexto)
    

def cargarJSON():
    with open('db.json') as file:
        datos = json.load(file)

    for empleado in datos['employees']:
        Empleado.objects.create(nombre=empleado['name'], apellido=empleado['last_name'], correo=empleado['email'], telefono=empleado['phone'])
        print('ID: ', empleado['id'])
        print('Nombre: ', empleado['name'])
        print('Apellido: ', empleado['last_name'])
        print('Correo: ', empleado['email'])
        print('Telefono: ', empleado['phone'])
        print('Registro Hecho')