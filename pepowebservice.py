import os
from flask import Flask, request

app = Flask(__name__)

# Ruta principal con formulario para ingresar el nombre
@app.route("/")
def hola_html():
    return """
    <html>
        <head>
            <title>Pepo Web Service</title>
            <style>
                body {
                    font-family: Arial, Helvetica, sans-serif;
                    background-color: #ffffff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                .container {
                    max-width: 400px;
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                }
                input[type="text"] {
                    padding: 10px;
                    margin-top: 10px;
                    width: 80%;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                }
                button {
                    margin-top: 15px;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Bienvenido a Pepo Web Service</h1>
                <form action="/saludo" method="post">
                    <input type="text" name="nombre" placeholder="Escribe tu nombre" required>
                    <br>
                    <button type="submit">Enviar</button>
                </form>
            </div>
        </body>
    </html>
    """

# Ruta que recibe el nombre y muestra el saludo
@app.route("/saludo", methods=["POST"])
def saludo():
    nombre = request.form.get("nombre", "Usuario")
    return f"""
    <html>
        <head>
            <title>Saludo</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>¡Hola, {nombre}! 🎉</h1>
            <p>Bienvenido a Pepo Web Service.</p>
            <a href="/">Volver al inicio</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
