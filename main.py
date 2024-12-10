from flask import Flask, Response
from zeep import Client
from flasgger import Swagger, swag_from
import threading
from spyne import Application, rpc, ServiceBase, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import time

# ------------- SOAP SERVER ----------------
class HelloWorldService(ServiceBase):
    @rpc(String, _returns=String)
    def say_hello(ctx, name):
        return f"Hello {name} from SOAP in python."

# SOAP application configuration
soap_app = Application(
    [HelloWorldService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

# Function to start SOAP server
def start_soap_server():
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP server running in: http://localhost:8000")
    print("Service available in: http://localhost:8000/?wsdl")
    server.serve_forever()

# Start the SOAP server in a separate thread
server_thread = threading.Thread(target=start_soap_server, daemon=True)
server_thread.start()

# ------------- FLASK CLIENT WITH SWAGGER ----------------
app = Flask(__name__)
swagger = Swagger(app)

@app.route("/")
@swag_from({
    'tags': ['SOAP Client'],
    'summary': 'Call SOAP say_hello method',
    'description': 'Sends a request to the SOAP server and retrieves the response.',
    'responses': {
        200: {
            'description': 'Successful response from SOAP server',
            'content': {
                'text/plain': {
                    'example': 'Hello World from SOAP in python.'
                }
            }
        },
        500: {
            'description': 'Error connecting to SOAP server',
            'content': {
                'text/plain': {
                    'example': 'Error while connecting to SOAP server: Connection refused'
                }
            }
        }
    }
})
def call_soap():
    """
    Endpoint to call the SOAP method 'say_hello'.
    """
    try:
        wsdl_url = "http://localhost:8000/?wsdl"
        client = Client(wsdl_url)
        response = client.service.say_hello("World")
        return Response(response, mimetype="text/plain")
    except Exception as e:
        return Response(f"Error while connecting to SOAP server: {str(e)}", status=500, mimetype="text/plain")

if __name__ == "__main__":
    # Allow some time for SOAP server to start
    time.sleep(2)
    print("Flask server running in http://localhost:5000")
    print(f"Swagger documentation at: \033[92mhttp://localhost:5000/apidocs\033[0m")
    app.run(host="0.0.0.0", port=5000, debug=True)
