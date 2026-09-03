# Guía del Proyecto APICARRO52

¡Hola, estudiante! Esta guía te ayudará a entender la estructura y el funcionamiento del proyecto `APICARRO52`. Este proyecto es una API (Interfaz de Programación de Aplicaciones) construida con **Python** y el framework **Flask**, y se conecta a una base de datos **MySQL**.

El proyecto sigue una arquitectura en capas similar al patrón **MVC** (Modelo-Vista-Controlador), separando las responsabilidades del código para que sea más fácil de mantener, escalar y entender.

A continuación, explicaremos qué hace cada capa (carpeta) y los archivos principales que la componen.

---

## 🏗️ Estructura del Proyecto (Capas)

### 1. `Models/` (Modelos)
Esta capa es responsable de definir la estructura de los datos que manejamos en la aplicación. Aquí creamos clases (programación orientada a objetos) que representan las tablas de nuestra base de datos.

*   **¿Qué hace?** Modela la información. Cada objeto creado a partir de estas clases representa un registro (una fila) en la base de datos.
*   **Archivo destacado: `user.py`**
    *   Contiene la clase `User`, la cual tiene atributos como id, nombre, apellido, documento, etc.
    *   Incluye un método muy útil llamado `to_dic(self)`. Este método convierte el objeto `User` en un diccionario de Python. Esto es crucial porque para enviar datos a través de la API (en formato JSON), primero necesitamos convertir los objetos a diccionarios.

### 2. `Routes/` (Rutas)
Esta capa se encarga de recibir las peticiones web (HTTP) que llegan a nuestra API desde el cliente (por ejemplo, un navegador web, Postman, o una aplicación móvil). Define las URLs (los "caminos") disponibles.

*   **¿Qué hace?** Escucha las solicitudes web en diferentes direcciones (como `/users/`) y métodos (GET, POST, PUT, DELETE) y decide a qué parte del código (Controlador) debe enviar esa solicitud para que sea procesada. Utiliza `Blueprints` de Flask para agrupar rutas de manera organizada.
*   **Archivos destacados:**
    *   **`__init__.py`**: Es el archivo principal de las rutas. Tiene la función `load_routes(app)` que se encarga de registrar (conectar) todas las rutas agrupadas (`Blueprints`) a la aplicación principal.
    *   **`UserRoutes.py`**: Define las rutas específicas para los usuarios. Por ejemplo, define que cuando llegue una petición `GET` a la ruta `/` (que internamente será `/users/`), debe llamar a la función `cntListUsers()` del Controlador.

### 3. `Controllers/` (Controladores)
Los controladores actúan como intermediarios (el pegamento) entre las Rutas (lo que pide el usuario) y los Servicios (la lógica del negocio).

*   **¿Qué hace?** Recibe la petición desde la Ruta, extrae cualquier información necesaria (como datos enviados en un formulario web), llama al Servicio correspondiente para hacer el trabajo pesado, y finalmente toma el resultado de ese servicio y lo prepara para enviarlo de vuelta al cliente (usualmente en formato JSON con la función `jsonify()`).
*   **Archivo destacado: `UserController.py`**
    *   Contiene funciones como `cntListUsers()`. Esta función no hace consultas a la base de datos directamente; simplemente llama a `servListUser()` (del Servicio), recibe los datos, y los empaqueta como una respuesta JSON exitosa (código 200).

### 4. `Services/` (Servicios)
Aquí es donde ocurre la "magia". Esta capa contiene toda la **lógica de negocio** y es la única que debería interactuar directamente con la base de datos (o con otros servicios externos).

*   **¿Qué hace?** Ejecuta las operaciones importantes: consultar, insertar, actualizar o eliminar datos en la base de datos MySQL. También realiza cálculos, validaciones complejas o procesos antes de devolver un resultado al Controlador.
*   **Archivo destacado: `UserService.py`**
    *   Contiene funciones como `servListUser()`. Esta función crea una conexión a la base de datos (`current_app.mysql.connection.cursor()`), escribe la consulta SQL (`SELECT * FROM T_USER`), la ejecuta, recoge los resultados y luego transforma cada fila devuelta por la base de datos en un objeto `User` (del Modelo) y luego en un diccionario usando `to_dic()`. Finalmente, devuelve esa lista de diccionarios al Controlador.

---

## ⚙️ Archivos Principales de Configuración

Además de las capas, hay archivos en la raíz del proyecto que son fundamentales para que todo arranque:

### `app.py` (Archivo Principal)
Es el corazón de la aplicación. Es el primer archivo que se ejecuta para iniciar el servidor.
*   **¿Qué hace?**
    1.  Crea la instancia de la aplicación Flask (`app = Flask(__name__)`).
    2.  Carga la configuración de la base de datos desde el archivo `config.py`.
    3.  Inicializa la conexión con MySQL (`mysql = MySQL(app)`).
    4.  Carga todas las rutas llamando a `load_routes(app)`.
    5.  Finalmente, arranca el servidor web (`app.run()`).

### `config.py` (Configuración)
Gestiona las variables de entorno (datos sensibles que no deben estar escritos directamente en el código fuente, como las contraseñas).
*   **¿Qué hace?** Utiliza la librería `dotenv` para leer un archivo oculto llamado `.env` (donde están guardadas las credenciales reales). Luego, crea una clase `Config` que contiene variables estáticas con el Host, Usuario, Contraseña y Puerto de tu base de datos MySQL. El archivo `app.py` lee esta clase para saber cómo conectarse a la base de datos.

### `.env` (Variables de Entorno - Oculto)
Este archivo (que no se suele subir a repositorios de código como GitHub por seguridad) contiene la configuración real de tu entorno local, por ejemplo:
```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=secreta
MYSQL_DATABASE=nombre_de_bd
```

### `requirements.txt`
Es un archivo de texto simple que lista todas las librerías o dependencias externas de Python que necesita tu proyecto para funcionar (como `Flask`, `Flask-MySQLdb`, `python-dotenv`). Los estudiantes usan este archivo para instalar todo rápidamente con el comando `pip install -r requirements.txt`.

---

## 🔄 Flujo de Trabajo: ¿Cómo viaja la información?

Para que lo entiendas mejor, imagina qué pasa cuando entras a `http://localhost:5000/users/` desde tu navegador:

1.  **Rutas (`UserRoutes.py`):** Flask detecta que has entrado a esa URL y busca quién debe atenderla. Encuentra que esa ruta apunta a la función `cntListUsers()` en el Controlador.
2.  **Controlador (`UserController.py`):** La función `cntListUsers()` toma el control. Su trabajo es responderte, pero no sabe cómo buscar los usuarios. Así que le pide ayuda a la capa de Servicios llamando a `servListUser()`.
3.  **Servicios (`UserService.py`):** La función `servListUser()` se conecta a MySQL, lanza la consulta `SELECT`, recibe los datos, usa los **Modelos** (`User`) para organizar la información en diccionarios y le devuelve esa lista limpia al Controlador.
4.  **Controlador (De vuelta):** Recibe la lista limpia del Servicio, la transforma en texto JSON (el formato universal de las APIs) usando `jsonify()` y la envía finalmente a tu navegador.

¡Y así es como funciona la API! Mantener el código separado en estas capas te permitirá trabajar en equipo y encontrar errores mucho más rápido.
