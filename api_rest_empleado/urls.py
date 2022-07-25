from django.urls import path
import api_rest_empleado.views

urlpatterns = [
    path('empleados_api_gp', api_rest_empleado.views.get_post_empleado, name="empleados_api_gp"),
    path('empleados_api_pd/<id>', api_rest_empleado.views.put_delete_empleado, name="empleados_api_pd"),
]