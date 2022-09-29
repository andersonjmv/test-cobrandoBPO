# test-cobrandoBPO
Prueba Técnica - Desarrollador Python Backend

Desarrollar un microservicio para la tabla empleados capaz de realizar las operaciones CRUD (Crear, Leer, Actualizar y Borrar), conectado a una base de datos PostgreSQL y por medio del puerto 1234

## Requisitos de despliegue
 
1. Descargar o clonar el repositorio en su computador local.

2. Una vez ubicado en la raiz del proyecto ejecutar el siguiente comando

```
pip install
```

3. Cambiar las credenciales de acceso de la base de datos con su base de datos local

```
/pruebatecnica/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'empleados',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
```

4. Ejecutar los siguientes comandos para migracion de estructuras a la base de datos local.

```
python manage.py makemigrations

python manage.py migrate
```

5. Ejecutar el servidor local

```
python manage.py runserver
```

5. Esto abrira una pestaña en su navegador en caso de que no se abra automaticamente ,tambien accediendo a esta [URL](https://127.0.0.1:1234/)

## Desarrollado con:

- [Python](https://www.python.org/) - Lenguaje interpretado de programaciòn Python.
- [Django](https://www.djangoproject.com/) - Framework para aplicaciones web con Python.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Herramienta para construir API con Django.
- [PostgresSQL](https://www.postgresql.org/) - Motor de base de datos SQL.

## Licencia 

Este proyecto está bajo la Licencia MIT.
