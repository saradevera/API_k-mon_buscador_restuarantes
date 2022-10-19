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

  # NOS CONECTAMOS A LA DB PARA OBTENER LA TABLA DE DATOS
    data = conn_db()

    info_from_type(data)
    info_from_description(data)
    new_columns(data)
    columnas_sumatorio(data)
    columnas_scoring(data)


    # RECIBIMOS LA INFO DE LA API DE NUESTRA WEB
    lista_pref = [2,4,3,1,2,2,2,3,1,1]
    # lista_pref = []
    
    data1 = data[[
            'place_name',
            'SCORE_vegano',
            'SCORE_vegetariano',
            'SCORE_sostenible',
            'SCORE_de_temporada',
            'SCORE_orgánico',
            'SCORE_saludable',
            'SCORE_fresco',
            'SCORE_artesano',
            'SCORE_cero_basura',
            'SCORE_de_proximidad'
            ]]

    for j in lista_pref:
        try:
            lista_result = []
            for i in data1.drop(columns=['place_name']).columns:
                result = data1[data1[i]>=lista_pref[j]]
                lista_result.append(result)
                final = pd.concat(lista_result, axis=0).drop_duplicates(subset='place_name')
        except:
            return '¡Lo siento! No hay resultados que se ajusten a tus preferencias'

    final = final.to_json(orient = 'index')

    # return str(final)
    return jsonify(final)



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
    data_ii = data.drop(columns=['place_name', 'type', 'resotie',
                                'place_id', 'address', 'phone',
                                'website', 'description', 'photos_link',
                                'thumbnail', 'is_spain', 'keywords', 'localidad'])

    # ESCALAMOS LOS DATOS Y CREAMOS LA MATRIZ
    ss = StandardScaler()
    data_scalado = ss.fit_transform(data_ii)
    # data_matrix = np.array(data_scalado)

    # CREAMOS EL COMPARATIVO DE DATOS Y EL INDICE QUE SE CONSULTARÁ
    cosine_sim = linear_kernel(data_scalado, data_scalado)
    index = pd.Series(data.index, index=data['place_name']).drop_duplicates()

    # GENERAMOS LA SIMILITUD COSENO Y SE ORDENA SEGÚN PARECIDOS
    place_name = str(data.iloc[ID]['place_name'])
    recomendacion = get_recommendations(place_name, index, data, cosine_sim)

    recomendacion = recomendacion.to_json(orient = 'index')

    return jsonify(recomendacion)
    # return str(recomendacion)


if __name__ == '__main__':
  app.run(threaded=True, port=5000)