from spyne import Application, rpc, ServiceBase, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import threading
from flask import Flask, Response
from zeep import Client

# ------------- SERVIDOR SOAP ----------------
class HelloWorldService(ServiceBase):
    @rpc(String, _returns=String)
    def say_hello(ctx, name):
        return f"Hola {name} desde SOAP en python."

# Configuración de la aplicación SOAP
soap_app = Application(
    [HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

# Función para iniciar el servidor SOAP
def start_soap_server():
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Servidor SOAP corriendo en http://localhost:8000")
    print("Servicio disponible en: http://localhost:8000/?wsdl")
    server.serve_forever()

# Iniciar el servidor SOAP en un hilo separado
server_thread = threading.Thread(target=start_soap_server, daemon=True)
server_thread.start()

# ------------- CLIENTE SOAP CON FLASK ----------------
app = Flask(__name__)

@app.route("/")
def call_soap():
    try:
        # Conexión al servidor SOAP usando Zeep
        wsdl_url = "http://localhost:8000/?wsdl"
        client = Client(wsdl_url)

        # Llamada al metodo SOAP say_hello
        response = client.service.say_hello("Mundo")

        # Devolver la respuesta como texto simple
        return Response(response, mimetype="text/plain")

    except Exception as e:
        return Response(f"Error al conectar con el servidor SOAP: {str(e)}", status=500, mimetype="text/plain")

if __name__ == "__main__":
    import time
    time.sleep(2)  # Espera a que el servidor SOAP esté disponible
    print("Servidor Flask corriendo en http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
