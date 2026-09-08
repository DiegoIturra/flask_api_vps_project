from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        "nombre": "Ana García",
        "edad": 28,
        "altura": 1.65,
        "descripcion": "Diseñadora gráfica",
    },
    {
        "nombre": "Luis Pérez",
        "edad": 34,
        "altura": 1.80,
        "descripcion": "Ingeniero de software",
    },
    {
        "nombre": "María López",
        "edad": 41,
        "altura": 1.58,
        "descripcion": "Docente de matemáticas",
    },
    {
        "nombre": "Carlos Ruiz",
        "edad": 25,
        "altura": 1.72,
        "descripcion": "Estudiante de medicina",
    },
    {
        "nombre": "Valentina Torres",
        "edad": 31,
        "altura": 1.70,
        "descripcion": "Abogada laboralista",
    },
]

FIELDS = ["nombre", "edad", "altura", "descripcion"]

@app.route("/", methods=["GET"])
def index():
    return jsonify({"mensaje": "API Flask", "endpoints": ["/health", "/users"]}), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "El cuerpo debe ser un JSON válido"}), 400

    missing = []
    for field in FIELDS:
        if field not in data or data[field] is None:
            missing.append(field)

    if missing:
        return jsonify(
            {"error": f"Los campos {', '.join(missing)} son obligatorios y no pueden ser nulos"}
        ), 400

    nuevo_usuario = {field: data[field] for field in FIELDS}
    users.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)