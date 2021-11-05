from flask import Flask, request
from Prediccion import predecir
import urllib.request

app = Flask(__name__)

@app.route("/predecirneumotorax", methods=["POST"])
def predecirPneumothorax():
    imagen = request.args.get("imagen")
    ruta = "./img/Neumotorax/imagen.jpg"
    urllib.request.urlretrieve(imagen,ruta)
    result = predecir.predecirPneumothorax(ruta)
    return result


@app.route("/predecirpneumonia", methods=["POST"])
def predecirPneumonia():
    imagen = request.args.get("imagen")
    ruta = "./img/Neumonia/imagen.jpg"
    urllib.request.urlretrieve(imagen,ruta)
    result = predecir.predecirneumonia(ruta)
    return result

@app.route("/")
def hello():
    return '<h1> API THESIS aa <h1>'

if __name__=="__main__":
  app.run() 
