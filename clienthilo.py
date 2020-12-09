#!"C:/Program Files/Python37/python.exe"
from flask import Flask, jsonify, send_file, request, render_template ,render_template_string, make_response, send_from_directory
from flask_cors import CORS, cross_origin
import flask
import threading
import time

#Includes de práctica:
from classes.Reloj import Reloj

app = Flask(__name__)

hilo = 2
relojes = []

#Esta ruta predeterminada lo redirije a /relojes
@app.route("/")
def goToMain():
    global hilo
    h = Reloj("#"+str(hilo))
    relojes.append(h)
    relojes[0].start()
    print("Inició hilo:",hilo)
    hilo+=1

    return flask.redirect("/relojes", code=302)

goToMain()
