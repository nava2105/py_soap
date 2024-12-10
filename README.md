# soap_flask_api
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
## General Info
***
This is a project built in Python that integrates a **SOAP server** using `Spyne` and a **Flask-based REST API** acting as a SOAP client. The project demonstrates communication between a SOAP service and a REST endpoint.
- The **SOAP server** responds to a `say_hello` method, returning a greeting message.
- The **Flask API** acts as a client, calls the SOAP server, and returns the response in plain text.
## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org): Version 3.12.0
* [Flask](https://flask.palletsprojects.com/en/stable/): Version 3.1.0
* [Spyne](https://spyne.io/): Version 2.13.16
* [Zeep](https://docs.python-zeep.org/en/latest/): Version 4.2.1
* [Swagger](https://swagger.io/docs): Version 0.0.2
## Installation
***
There are two methods to install this project.
### Via GitHub
Verify you are python version 3.12.0
```
python --version
```
Copy the repository
```
git clone https://github.com/nava2105/py_soap.git
```
Enter the directory
```
cd ../py_soap
```
Create a virtual environment
```
python -m venv .venv
```
Activate your virtual environment
* In Windows
```
.venv\Scripts\activate
```
In macOS or Linux
```
source .venv/bin/activate
```
Build the dependencies
```
pip install -r requirements.txt
```
Run main.py file
* By using python command
```
python main.py
```
* If you are using Python 3 and python points to Python 2 on your system, use python3 instead:
```
python3 main.py
```
Open a browser and enter to
* Server: [http://localhost:8000](http://localhost:8000)
* Service: [http://localhost:8000/?wsd](http://localhost:8000/?wsd)
* Client:[http://localhost:5000](http://localhost:5000)
* Swagger:[http:localhost:5000/apidocs](http:localhost:5000/apidocs)
### Via Docker-hub
Pull the image from Docker-hub
```
docker pull na4va4/py_soap
```
Start a container from the image
```
docker run -p 5000:5000 -p 8000:8000 na4va4/py_soap
```
Open a browser and enter to
* Server: [http://localhost:8000](http://localhost:8000)
* Service: [http://localhost:8000/?wsd](http://localhost:8000/?wsd)
* Client:[http://localhost:5000](http://localhost:5000)
* Swagger:[http:localhost:5000/apidocs](http:localhost:5000/apidocs)