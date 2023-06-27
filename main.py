from flask import Flask,jsonify,render_template
import socket
#from flask_restful import Resource, Api
app = Flask(__name__)

def fetchdetails():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)

@app.route("/")
def ping_server():
    return("Welcome to python-Flash Docker Kubernetes Demo")

@app.route("/details")
def detail():
    hostname,ip=fetchdetails()
    return render_template('index.html',HOSTNAME=hostname,IP=ip)
        
         
        

@app.route("/food")

def get():
    return jsonify(
    {
        "id": 1,
        "name": "corn",
        "type": "local"
    },
    {
        "id": 2,
        "name": "Cornflakes",
        "type": "modern"
    },
    {
        "id": 3,
        "name": "indolmie",
        "type": "modern"
    },
    {
        "id": 4,
        "name": "gari",
        "type": "local"
    },
    {
        "id": 5,
        "name": "chicken",
        "type": "good"
    },
    {
        "id": 6,
        "name": "goat",
        "type": "local_animal"
    },
);
    
   
		

if __name__ == '__main__':
	app.run(debug=True, port=5004,host="0.0.0.0")