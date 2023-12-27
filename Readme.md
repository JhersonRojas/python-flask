# API REST con Flask - Proyecto Backend

## Descripción
Este proyecto consiste en el desarrollo de una API REST utilizando Flask, un framework web de Python. 

La API proporciona endpoints para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre recursos específicos, siguiendo las convenciones RESTful.

## Características
- **Endpoints RESTful:** Implementa endpoints para realizar operaciones CRUD sobre recursos específicos.
- **Serialización de datos:** Utiliza bibliotecas como Flask-RESTful o Flask-RestPlus para serializar datos en formato JSON.

## Requisitos
- Conocimientos básicos de Python
- Familiaridad con conceptos de API REST

## Estructura de Directorios
- **`src/app.py`:** Punto de entrada de la aplicación Flask.
- **`routes/`:** Carpeta que contiene los archivos con las rutas y lógica de la API.
- **`utils/`:** Directorio opcional para funciones o utilidades auxiliares.
- **`venv/`:** Entorno virtual para gestionar las dependencias del proyecto.

## Uso
1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual: `python -m venv venv`.
3. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`
4. Instala las dependencias: `pipenv install`.
5. Configura la base de datos si es necesaria.
6. Ejecuta la aplicación: `pipenv run dev`.
7. Utiliza herramientas como Postman o cURL para interactuar con los endpoints de la API.

## Recursos Adicionales
- [Documentación oficial de Flask](https://flask.palletsprojects.com/)
- Tutoriales y libros sobre la creación de API REST con Flask.
