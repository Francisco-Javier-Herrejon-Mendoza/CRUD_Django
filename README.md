# CRUD_Django

Para inicializar el proyecto, se debe crear una base de datos en postgresql llamada crud_django. Y para conectar el proyecto con la base de datos, se debe cambiar
la contraseña actual en settings a la contraseña que se tiene localmente en el postgresql a utilizar.

Se debe correr el siguiente comando: python manage.py makemigrations

Posteriormente se debe correr el siguiente comando: python manage.py migrate

Y una vez lista la base de datos, se debe agregar un registro a la tabla de bandera, de manera directa en la base de datos en postgresql seria:
INSERT INTO public.bandera (nombre, valor) VALUES ("Funcion cargar JSON", 0);

Se puede crear un super usuario para entrar al admin de django con el comando: python manage.py createsuperuser

Y se hizo un deploy en heroku del proyecto, el enlace para entrar es el siguiente: https://deploy-crud-django.herokuapp.com/
En caso de la aplicacion en heroku deje de funcionar, favor de mandarme un correo a: fherrejon10@gmail.com

Gracias.
