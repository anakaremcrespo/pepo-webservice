import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/saludo", methods=["POST"])
def saludo_html():
    nombre = request.form.get("nombre", "Usuario")
    return f"""
    <html>
        <head><title>Saludo</title></head>
        <body style="text-align:center; margin-top:50px; font-family:Arial;">
            <h1>¡Hola, {nombre}! 🎉</h1>
            <p>Bienvenido a Pepo Web Service.</p>
            <a href="/">Volver al inicio</a>
        </body>
    </html>
    """

@app.route("/saludo_json", methods=["POST"])
def saludo_json():
    def saludo_json():
    data = request.get_json()  # aquí recibe un JSON {"nombre": "Pepo"}
    nombre = data.get("nombre", "Usuario") if data else "Usuario"
    return jsonify({"mensaje": f"¡Hola, {nombre}! Bienvenido a Pepo Web Service 🎉"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
