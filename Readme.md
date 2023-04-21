# API documentation
- Dependencies:
    - anyio
    - click
    - colorama
    - fastapi
    - h11
    - idna
    - numpy
    - opencv-python
    - pycodestyle
    - pydantic
    - sniffio
    - starlette
    - typing_extensions
    - uvicorn
- Dev Dependencies:
    - autopep8

## Run aplication 

### Install 
1. python
2. vscode

### Run 

1. Crea un entorno virtual en la carpeta de trabajo: terminal>nueva terminal

        python -m venv myvenv

2. instalar las dependencias en el entorno virtual de la carpeta de trabajo

        pip install -r requirements.txt

3. Correr el servidor en un host local (Verifica que no se empate con un puerto ya utilizado por otra aplicacion)

        uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

4. Has los fetch correspondientes

- depende de tu aplicación lo puedes hacer a 0.0.0.0 o a 127.0.0.1
- Si hay un error con la petición sobre el servidor, es decir que no puede responderte porque no estás en la lista de aceptados como servicio prueba agregar tu puerto de entrada a la lista ubicada en main.py origins

~~~python 
origins = [
    "*",
    "tu origen",
    "http://localhost:8080",
]
~~~

# Miscelaneus

Los tres niveles del modelo de madurez de Richardson para API REST son los siguientes:

1. Nivel 0 - POX (Plain Old XML): 

- Este nivel es el más básico y no cumple con ninguna de las restricciones de Fielding. Las aplicaciones en este nivel utilizan HTTP como un simple canal de transporte para enviar y recibir mensajes XML.

2. Nivel 1 - RESTful Resources: 

- Este nivel introduce el concepto de recursos y la identificación de recursos a través de URIs. Las aplicaciones en este nivel utilizan HTTP para acceder a los recursos y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en ellos.

3. Nivel 2 - HTTP Verbs: 

- Este nivel introduce el uso correcto de los verbos HTTP para realizar operaciones CRUD en los recursos identificados por URIs. Las aplicaciones en este nivel utilizan los verbos HTTP GET, POST, PUT y DELETE para realizar operaciones CRUD en los recursos.

4. Nivel 3 - HATEOAS (Hypermedia as the Engine of Application State): 

- Este nivel introduce la idea de que los recursos deben contener enlaces a otros recursos relacionados. Las aplicaciones en este nivel utilizan los enlaces para navegar por la aplicación y realizar operaciones CRUD en los recursos.