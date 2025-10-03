import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Pepo Web Service</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #4facfe, #00f2fe);
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #333;
                }
                .card {
                    background: #fff;
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2);
                    text-align: center;
                    width: 350px;
                }
                h1 {
                    color: #4facfe;
                    margin-bottom: 20px;
                }
                input[type="text"] {
                    padding: 12px;
                    width: 80%;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    font-size: 14px;
                }
                button {
                    padding: 12px 20px;
                    background: #4facfe;
                    color: white;
                    font-size: 14px;
                    border: none;
                    border-radius: 10px;
                    cursor: pointer;
                    transition: background 0.3s ease;
                }
                button:hover {
                    background: #00c6ff;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Bienvenido a Pepo Web Service</h1>
                <p>Ingresa tu nombre para ser parte de Macrocom</p>
                <form action="/saludo" method="post">
                    <input type="text" name="nombre" placeholder="Ingresa tu nombre" required>
                    <br>
                    <button type="submit">Enviar</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.route("/saludo", methods=["POST"])
def saludo_html():
    nombre = request.form.get("nombre", "Usuario")
    return f"""
    <html>
        <head>
            <title>Saludo</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0;
                }}
                .card {{
                    background: #fff;
                    padding: 30px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
                    width: 350px;
                }}
                h1 {{
                    color: #ff6a88;
                }}
                a {{
                    display: inline-block;
                    margin-top: 15px;
                    text-decoration: none;
                    color: #fff;
                    background: #ff6a88;
                    padding: 10px 15px;
                    border-radius: 10px;
                    transition: background 0.3s ease;
                }}
                a:hover {{
                    background: #ff99ac;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>¡Hola, {nombre}!</h1>
                <p>Bienvenido a Pepo Web Service.</p>
                <a href="/">Regresar a la página de inicio</a>
            </div>
        </body>
    </html>
    """

# Ruta JSON
@app.route("/saludo_json", methods=["POST"])
def saludo_json():
    data = request.get_json()
    nombre = data.get("nombre", "Usuario") if data else "Usuario"
    return jsonify({"mensaje": f"¡Hola, {nombre}! Bienvenido a Pepo Web Service, ya eres parte de Macrocom"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

