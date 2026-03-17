from flask import Flask, send_file, jsonify, request
import sqlite3  # importamos sqlite3 para usar la base de datos

app = Flask(__name__)

# ─── FUNCIÓN: abrir conexión a la base de datos ───
def conectar():
    conn = sqlite3.connect("tareas.db")  # crea o abre el archivo tareas.db
    conn.row_factory = sqlite3.Row       # hace que los resultados se comporten como diccionarios
    return conn                          # regresa la conexión para usarla

# ─── FUNCIÓN: crear la tabla si no existe ───
def iniciar_db():
    conn = conectar() #ABRE LA CONEXXION
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL
        )
    """) # CRE LA TABLA DE TAREAS SI NO EXISTE
    conn.commit() # Guarda en automatico los cambiods
    conn.close() # CIERRRA LA CONEXION

# ─── RUTA: página principal ───
@app.route("/")
def index():
    return send_file("index.html")       # manda el archivo HTML al navegador

# ─── RUTA: obtener todas las tareas (GET) ───
@app.route("/tareas")
def obtener_tareas():
    conn = conectar()                    # abre la conexión
    tareas = conn.execute("SELECT * FROM tareas").fetchall()  # trae todas las tareas de la tabla
    conn.close()                         # cierra la conexión
    return jsonify([dict(t) for t in tareas])  # convierte cada tarea a diccionario y manda como JSON

# ─── RUTA: agregar tarea nueva (POST) ───
@app.route("/tareas", methods=["POST"])
def agregar_tarea():
    nueva = request.get_json()           # recibe el JSON que mandó JS
    conn = conectar()                    # abre la conexión
    conn.execute(                        
        "INSERT INTO tareas (titulo) VALUES (?)",  # inserta una tarea nueva en la tabla
        (nueva["titulo"],)               # el título que mandó JS
    )
    conn.commit()                        # confirma el cambio, lo guarda de verdad
    conn.close()                         # cierra la conexión
    return jsonify({"mensaje": "Tarea agregada"})  # responde a JS

if __name__ == "__main__":
    app.run(debug=True)                  # arranca el servidor