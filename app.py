from flask import Flask, request, jsonify, render_template
# import os
import sqlite3
import pandas as pd
import numpy as np
import pymysql
from functions import *
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import linear_kernel

# os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return render_template('hola.html')


@app.route("/RecomendacionPorPreferencias", methods = ['GET'])
def RecomendacionPorPreferencias():
    pref = request.get_json()["preferencias"]
  # NOS CONECTAMOS A LA DB PARA OBTENER LA TABLA DE DATOS
    data = conn_db()

    data = info_from_type(data)
    data = info_from_description(data)
    data = new_columns(data)
    data = columnas_sumatorio(data)
    data = columnas_scoring(data)
    # RECIBIMOS LA INFO DE LA API DE NUESTRA WEB
    recomendaciones = preferencias(pref, data)

    # return str(final)
    return recomendaciones

@app.route("/RecomendacionDependiente", methods = ['GET'])
def RecomendacionDependiente():

    # NOS CONECTAMOS A LA DB PARA OBTENER LA TABLA DE DATOS
    data = conn_db()

    info_from_type(data)
    info_from_description(data)
    new_columns(data)
    columnas_sumatorio(data)
    columnas_scoring(data)

    ID = int(request.args.get("ID"))

    # ELIMINAMOS LAS COLUMNAS QUE NO SON NECESARIAS EN ESTA FASE
    data.drop(columns=['place_name', 'type', 'resotie',
                                'place_id', 'address', 'phone',
                                'website', 'description', 'photos_link',
                                'thumbnail', 'is_spain', 'keywords', 'localidad', "index"], inplace = True)

    # ESCALAMOS LOS DATOS Y CREAMOS LA MATRIZ
    ss = StandardScaler()
    data_scalado = ss.fit_transform(data)
    # CREAMOS EL COMPARATIVO DE DATOS Y EL INDICE QUE SE CONSULTARÁ
    # GENERAMOS LA SIMILITUD COSENO Y SE ORDENA SEGÚN PARECIDOS
    recomendaciones = get_recommendations(ID, data_scalado)
    return recomendaciones
    # return str(recomendacion)


if __name__ == '__main__':
  app.run(threaded=True, port=5000)