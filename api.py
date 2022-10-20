from flask import Flask, request, jsonify, render_template
# import os
import sqlite3
import pandas as pd
import numpy as np
import pymysql
from functions import *
# from flask_cors import CORS, cross_origin
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import linear_kernel

# os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True


# CORS(app)
# CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=['GET'])
def hello():
    return render_template('hola.html')



# @app.route("/RecomendacionPorPreferencias", methods = ['POST'])
# def RecomendacionPorPreferencias():
#   pref = request.get_json()["preferencias"]
#   filtro = request.args.get("Filtro")
#   # NOS CONECTAMOS A LA DB PARA OBTENER LA TABLA DE DATOS
#   data = conn_db()

#   data = info_from_type(data)
#   data = info_from_description(data)
#   data = new_columns(data)
#   data = columnas_sumatorio(data)

#   if filtro == "restaurantes":
#     data = data[data["resotie"] == "Restaurante"]
#   elif filtro == "tiendas":
#     data = data[data["resotie"] == "Tienda"]
#   elif filtro == "todos":
#     pass
#   # RECIBIMOS LA INFO DE LA API DE NUESTRA WEB
#   recomendaciones = preferencias(pref, data)
#   recomendacionesDef= [int(x) for x in recomendaciones]
#   return str(recomendacionesDef)[1:-1]



# @app.route("/RecomendacionDependiente", methods = ['GET'])

# def RecomendacionDependiente():
#   filtro = request.args.get("Filtro")
#   ID = int(request.args.get("ID"))
#     # NOS CONECTAMOS A LA DB PARA OBTENER LA TABLA DE DATOS
#   data = conn_db()
#   data = info_from_type(data)
#   data = info_from_description(data)
#   data = new_columns(data)
#   data = columnas_sumatorio(data)
#   if filtro == "restaurantes":
#     data = data[data["resotie"] == "Restaurante"]
#   elif filtro == "tiendas":
#     data = data[data["resotie"] == "Tienda"]
#   elif filtro == "todos":
#     pass
#   # ELIMINAMOS LAS COLUMNAS QUE NO SON NECESARIAS EN ESTA FASE
#   index = [x for x in data["index"]]
#   indice_matriz = index.index(ID)
#   data.drop(columns=['place_name', 'type', 'resotie',
#                               'place_id', 'address', 'phone',
#                               'website', 'description', 'photos_link',
#                               'thumbnail', 'is_spain', 'keywords', 'localidad', "index"], inplace = True)
  
#   # ESCALAMOS LOS DATOS Y CREAMOS LA MATRIZ
#   ss = StandardScaler()
#   data_scalado = ss.fit_transform(data)
#   # CREAMOS EL COMPARATIVO DE DATOS Y EL INDICE QUE SE CONSULTARÁ
#   # GENERAMOS LA SIMILITUD COSENO Y SE ORDENA SEGÚN PARECIDOS
#   recomendaciones = get_recommendations(data_scalado, indice_matriz)
#   return str(recomendaciones)[1:-1]


if __name__ == '__main__':
  app.run(threaded=True, port=5000)