# API de ferreteria con Django Rest Framework

Esta es una API para una ferretería que permite acceder y gestionar items de ferretería.

## Instalación:

1. Clona este repositorio:

```
git clone https://github.com/Alan1657/pythonApi.git
cd ferreteria_api
```
2. Crea un entorno virtual e instala las dependencias:

```
python -m venv venv

# Activación en Unix
source venv/bin/activate

# Activación en Windows
venv\Scripts\activate

pip install -r requirements.txt
```
3. Configura la base de datos y aplica las migraciones:
```
python manage.py migrate
```
4. Inicia el servidor de desarrollo:

```
python manage.py runserver
```
5. Crea un superusuario de ser necesario:

```
Para crear un super usuario y acceder al admin:
make createsuperuser
```
## Base de datos:

Esto proyecto requiere que tenga instalado MySQL.
Actualice los datos de la base de datos que quiere utilizar en `settings/locale.py`.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_base_de_datos',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'host',
        'PORT': 'port'
    }
}
```
