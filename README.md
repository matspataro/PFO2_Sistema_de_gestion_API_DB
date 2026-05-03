# Sistema de Gestion de Tareas - API Backend

Este proyecto implementa un sistema de gestión de usuarios y tareas desarrollado con Python y el framework Flask. La aplicación permite el registro y la autenticación de usuarios utilizando una base de datos SQLite y técnicas de seguridad mediante el hasheo de contraseñas.

## Configuracion del Entorno

Para preparar el entorno de ejecucion, ejecute los siguientes comandos en la terminal del editor

1. **Creacion y activacion del entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Linux/Mac:
    source venv/bin/activate
    ```

## Instalacion de dependencias

Con el entorno virtual activo, utilice el gestor de paquetes pip para instalar las librerias especificadas en el archivo de requerimientos del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecucion del Servidor

Para iniciar la aplicacion, ejecute el script principal desde la terminal:

    ```bash
    python servidor.py
    ```

El servidor comenzara a funcionar en http://127.0.0.1:5000. Al realizar la primera ejecucion, el sistema invocara automaticamente la funcion de inicializacion para configurar la base de datos gestion_tareas.db y las tablas de usuario necesarias.

## Endpoints de la API

La aplicacion expone los siguientes puntos de acceso para interactuar con el sistema de gestion de usuarios y tareas:

| Endpoint | Metodo | Descripcion |
| :--- | :--- | :--- |
| `/registro` | POST | Permite registrar un nuevo usuario almacenando la contraseña mediante hashing. |
| `/login` | POST | Valida las credenciales del usuario contra la base de datos SQLite. |
| `/tareas` | GET | Renderiza una vista dinamica de bienvenida utilizando el motor de plantillas Jinja2. |

### Formato de datos para peticiones POST

Para los endpoints de registro e inicio de sesion, se debe enviar un objeto JSON con la siguiente estructura:

    ```json
    {
    "usuario": "nombre_de_usuario",
    "contraseña": "tu_clave"
    }
    ```

---
Matías Spataro -
Proyecto academico para la Tecnicatura en Desarrollo de Software - IFTS N° 29.