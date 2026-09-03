# Estandarización de nombres del proyecto

Este proyecto usa una convención de nombres clara para mantener el código organizado, legible y fácil de mantener.

> Nota: los archivos de controladores, rutas y servicios usan PascalCase.

## 1. Estructura recomendada

```text
app.py
config.py
requirements.txt
README.md

Controllers/
  UserController.py
  CarController.py

Models/
    user.py
    car.py

Routes/
  UserRoutes.py
  CarRoutes.py
    __init__.py

Services/
  UserService.py
  CarService.py
```

## 2. Convenciones generales

### Nombres de carpetas
- Las carpetas deben ir en singular y en minúsculas:
  - `Controllers`
  - `Models`
  - `Routes`
  - `Services`

### Archivos
- Los archivos de controladores, rutas y servicios deben usar PascalCase:
  - `UserController.py`
  - `CarController.py`
  - `UserRoutes.py`
  - `CarRoutes.py`
  - `UserService.py`
  - `CarService.py`

### Clases
- Los nombres de clase deben usar PascalCase:
  - `UserController`
  - `CarController`
  - `User`
  - `Car`

### Variables y funciones
- Las funciones deben usar snake_case:
  - `list_users()`
  - `create_user()`
  - `update_user()`
  - `delete_user()`

- Las variables deben usar snake_case:
  - `user_name`
  - `car_model`
  - `document_number`

### Blueprints y rutas
- Los Blueprints deben nombrarse con el recurso seguido de `_bp`:
  - `user_bp`
  - `car_bp`

- Las rutas deben estar alineadas con el recurso principal:
  - `/users`
  - `/cars`

## 3. Regla recomendada por capa

### Controllers
Los archivos dentro de `Controllers` deben llamarse según el recurso:

```python
# Controllers/UserController.py
class UserController:
    def list_users(self):
        pass
```

### Models
Los modelos deben representar la entidad de negocio:

```python
# Models/user.py
class User:
    def __init__(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
```

### Routes
Los archivos de rutas deben encargarse de registrar endpoints:

```python
# Routes/UserRoutes.py
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def list_users():
    return ""
```

### Services
Los servicios deben contener la lógica de negocio y acceso a datos:

```python
# Services/UserService.py
class UserService:
    def list_users(self):
        pass
```

## 4. Estándar propuesto para este proyecto

Para mantener consistencia con Flask y Python, se recomienda este patrón:

- `Controllers/`: `UserController.py`, `CarController.py`
- `Models/`: `user.py`, `car.py`
- `Routes/`: `UserRoutes.py`, `CarRoutes.py`
- `Services/`: `UserService.py`, `CarService.py`

### Ejemplo de nomenclatura final

```text
Controllers/
  UserController.py
  CarController.py

Models/
    user.py
    car.py

Routes/
  UserRoutes.py
  CarRoutes.py

Services/
  UserService.py
  CarService.py
```

## 5. Reglas de estilo a seguir

1. Usar `PascalCase` para archivos de controladores, rutas y servicios.
2. Usar `PascalCase` para clases.
3. Mantener nombres descriptivos del recurso.
4. Evitar nombres genéricos como `datos.py`, `archivo.py` o `main.py`.
5. Mantener consistencia entre carpeta, archivo y clase.
6. Un recurso debe nombrarse igual en todos los niveles.

## 6. Recomendación final

La convención ideal para este proyecto es:

- `user` para usuarios
- `car` para autos
- `controller` para lógica de endpoints
- `service` para lógica de negocio
- `bp` para Blueprints

Con esto, el proyecto tendrá un orden más limpio y será más fácil de escalar.

## 7. Siguiente paso

Cuando se decida, se puede aplicar este estándar realizando el renombrado de los archivos y sus imports de manera ordenada, sin afectar la funcionalidad principal.
