import requests

BASE_URL = "http://127.0.0.1:5000"

# Funciones para interactuar con el servidor
def registrar_usuario():
    print("\n--- Registro de Nuevo Usuario ---")
    usuario = input("Ingrese nombre de usuario: ")
    contrasena = input("Ingrese contraseña: ")
    
    payload = {
        "usuario": usuario,
        "contraseña": contrasena
    }
    
    try:
        response = requests.post(f"{BASE_URL}/registro", json=payload)
        datos = response.json()

        # Registrar el mensaje de éxito o error del servidor
        resultado = datos.get('mensaje') or datos.get('error') or "Sin detalle del servidor"
        
        if response.status_code == 201:
            print(f"Éxito (201): {resultado}")
        else:
            print(f"Servidor respondió con error ({response.status_code}): {resultado}")
            
    except Exception as e:
        print(f"Error de conexion: {e}")

def iniciar_sesion():
    print("\n--- Inicio de Sesion ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    payload = {
        "usuario": usuario,
        "contraseña": contrasena
    }
    
    try:
        response = requests.post(f"{BASE_URL}/login", json=payload)
        if response.status_code == 200:
            print(f"Exito: Bienvenido {usuario}")
            # Si el login es correcto, accedemos al portal de tareas
            acceder_portal(usuario)
        else:
            print("Error: Credenciales invalidas.")
    except Exception as e:
        print(f"Error de conexion: {e}")

def acceder_portal(usuario):
    try:
        # Llamamos al endpoint que renderiza el HTML
        response = requests.get(f"{BASE_URL}/tareas", params={"nombre": usuario})
        if response.status_code == 200:
            print("Acceso concedido al portal de tareas.")
            print(f"URL del portal: {response.url}")
        else:
            print("No se pudo acceder al portal.")
    except Exception as e:
        print(f"Error al conectar con el portal: {e}")

def menu():
    while True:
        print("\n=== SISTEMA DE GESTION DE TAREAS ===")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Finalizando programa. ¡Hasta luego!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menu()