from flask import Flask, send_file, jsonify, request

app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Comprar leche"},
    {"id": 2, "titulo": "Estudiar Flask"},
    {"id": 3, "titulo": "Hacer ejercicio"}
]

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/tareas")
def obtener_tareas():
    return jsonify(tareas)

@app.route("/tareas", methods=["POST"])
def agregar_tarea():
    nueva = request.get_json()
    nueva["id"] = len(tareas) + 1
    tareas.append(nueva)
    return jsonify({"mensaje": "Tarea agregada"})

if __name__ == "__main__":
    app.run(debug=True)