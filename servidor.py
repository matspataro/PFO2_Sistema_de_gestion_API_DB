import sqlite3
from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = 'gestion_tareas.db'
app = Flask(__name__)

# Función para inicializar la base de datos y crear la tabla de usuarios
def inicializar_db():
    try:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    usuario TEXT NOT NULL UNIQUE, 
                    password_hash TEXT NOT NULL
                )
            ''')
        print("Base de datos inicializada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
        exit(1)

def ejecutar_consulta(query, params=()):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor

# Ruta para registrar un nuevo usuario
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    try:
        data = request.get_json()
        usuario = data.get('usuario')
        password = data.get('contraseña')

        if not usuario or not password:
            return jsonify({"error": "Faltan datos"}), 400

        hash_seguro = generate_password_hash(password)

        ejecutar_consulta("INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)", 
            (usuario, hash_seguro))
        
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

    except sqlite3.IntegrityError:
        # Error específico: el usuario ya existe 
        return jsonify({"error": "El nombre de usuario ya existe"}), 409
    except Exception as e:
        # Otros errores
        return jsonify({"error": "Ocurrió un error inesperado", "detalle": str(e)}), 500

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login_usuario():
    try:
        data = request.get_json()
        usuario = data.get('usuario')
        password = data.get('contraseña')

        if not usuario or not password:
            return jsonify({"error": "Faltan datos"}), 400

        cursor = ejecutar_consulta("SELECT password_hash FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

        if resultado and check_password_hash(resultado[0], password):
            return jsonify({"mensaje": f"Bienvenido, {usuario}"}), 200
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 401

    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado", "detalle": str(e)}), 500

# Ruta para mostrar la página de inicio 
@app.route('/tareas')
def tareas():
    nombre_usuario = request.args.get('nombre', 'Invitado')
    return render_template('tareas.html', usuario=nombre_usuario)

# Inicio del servidor y de la base de datos
if __name__ == "__main__":
    inicializar_db()
    app.run(debug=True, port=5000)