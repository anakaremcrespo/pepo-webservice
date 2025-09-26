import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hola_html():
    return """
    <html>
        <head>
            <title>Pepo Web Service</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #ffffff; /* Fondo blanco */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                h1 {
                    color: #333333;
                    font-size: 36px;
                    margin: 0;
                }
                p {
                    color: #555555;
                    font-size: 24px;
                    margin: 10px 0 0 0;
                }
            </style>
        </head>
        <body>
            <div>
                <h1>Bienvenidos a Pepo Web Service</h1>
                <p>Ana Karem Crespo López - 22031437</p>
            </div>
        </body>
    </html>
    """

@app.route("/json")
def hola_json():
    return jsonify({
        "mensaje": "Bienvenidos a Pepo Web Service",
        "nombre": "Ana Karem Crespo López - 22031437"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
