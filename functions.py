import pandas as pd
import numpy as np
import pymysql


def conn_db():
    # NOS CONECTAMOS A LA DB PARA OBTENER LA TABLA DE DATOS
    username = "admin"
    password = "12345678"
    host = "database-1.cjhgutfjw0tz.us-east-1.rds.amazonaws.com"

    db = pymysql.connect(host = host,
                      user = username,
                      password = password,
                      cursorclass = pymysql.cursors.DictCursor
    )

    cursor = db.cursor()

    use_db = ''' USE DB_negocios'''
    cursor.execute(use_db)

    cursor.execute("select * from negocios")
    data = pd.DataFrame(cursor.fetchall())

    db.close()

    return data

def info_from_type(data):
    # EXTRAEMOS INFO DE LA COLUMNA TYPE
    data['vegano 1'] = np.where(data['type'].str.contains('egan'), 1, 0)
    data['vegetariano 1'] = np.where(data['type'].str.contains('egeta'), 1, 0)
    data['orgánico 1'] = np.where(data['type'].str.contains('rgáni'), 1, 0)
    data['sostenible 1'] = np.where(data['type'].str.contains('osten'), 1, 0)
    data['frescos 1'] = np.where(data['type'].str.contains('grícol'), 1, 0)
    data['huerta 1'] = np.where(data['type'].str.contains('uert'), 1, 0)
    data['restaurante 1'] = np.where(data['type'].str.contains('estaurante'), 1, 0)
    data['tienda 1'] = np.where(data['type'].str.contains('ienda'), 1, 0)
    data['bar 1'] = np.where(data['type'].str.contains('Bar'), 1, 0)
    data['tienda 1'] = np.where(data['type'].str.contains('ienda'), 1, 0)
    
    return data


def info_from_description(data):
# EXTRAEMOS INFO DE LA COLUMNA DESCRIPTION
    data['vegetariano 2'] = np.where(data['description'].str.contains('egeta'), 1, 0)
    data['vegano 2'] = np.where(data['description'].str.contains('egan'), 1, 0)
    data['orgánico 2'] = np.where(data['description'].str.contains('rgáni'), 1, 0)
    data['saludable 2'] = np.where(data['description'].str.contains('alud'), 1, 0)
    data['sostenible 2'] = np.where(data['description'].str.contains('osten'), 1, 0)
    data['frescos 2'] = np.where(data['description'].str.contains('grícol'), 1, 0)
    data['huerta 2'] = np.where(data['description'].str.contains('uert'), 1, 0)
    data['vino 2'] = np.where(data['description'].str.contains('inos'), 1, 0)
    data['proximidad 2'] = np.where(data['description'].str.contains('roximidad'), 1, 0)
    data['local 2'] = np.where(data['description'].str.contains('ocal'), 1, 0)
    data['artesano 2'] = np.where(data['description'].str.contains('rtesan'), 1, 0)
    data['granel 2'] = np.where(data['description'].str.contains('ranel'), 1, 0)
    data['temporada 2'] = np.where(data['description'].str.contains('emporad'), 1, 0)

    return data


def new_columns(data):
# UNIFICAMOS COLUMNAS SEGÚN TEMÁTICA

    data['vegan'] = data['veganas'] + data['vegano'] + data['crudiveganismo'] + data['crueldad'] + data['heura'] + data['hamburguesa_vegana']
    data.drop(columns=['veganas', 'vegano', 'crudiveganismo', 'crueldad', 'heura'], inplace=True)

    data['vegetarian'] = data['vegan'] + data['vegetarianos'] + data['vegetales']
    data.drop(columns = ["vegetarianos", 'vegetales'], inplace=True)

    data['healthy'] =  data['salud'] + data['sano']  + data[ 'smoothies'] + data['integral']  + data['saludable'] + data['saludable 2']
    data.drop(columns=[ 'salud', 'sano', 'smoothies', 'integral'], inplace=True)

    data['seasonal'] = data['temporada'] + data['huerto'] + data['granja']
    data.drop(columns=['temporada', 'huerto', 'granja'], inplace=True)

    data['sustainable'] = + data['eficiente'] + data['justa'] +  data['cooperativa'] + data['ética'] + data['agricultores'] 
    data.drop(columns=['eficiente', 'justa', 'cooperativa', 'ética', 'agricultores'], inplace=True)

    data['handcrafted'] = data['artesanal'] + data['tradicional'] + data['tradición']
    data.drop(columns=['artesanal', 'tradicional', 'tradición'], inplace=True)

    data['organic'] = data['orgánico'] 
    data.drop(columns=['orgánico'], inplace=True)

    data['zero_waste'] =  data['reciclados'] + data['reciclaje'] + data['reciclar'] + data['biodegradables'] 
    data.drop(columns=['reciclados','reciclaje','reciclar', 'biodegradables'], inplace=True)

    data['alergens'] = data['alérgenos'] + data['gluten']  + data['lactosa'] + data['celíacos']
    data.drop(columns=['alérgenos', 'gluten',  'lactosa', 'celíacos'], inplace=True)

    data['wine'] = data['vino'] + data['maridaje'] + data['cavas']
    data.drop(columns=['vino', 'maridaje', 'cavas'], inplace=True)

    data['bread'] = data['obrador'] + data['palmera'] + data['palmeritas'] + data['bollería'] + data['horno'] + data['masa']
    data.drop(columns=['obrador','palmera', 'palmeritas', 'bollería', 'horno', 'masa'], inplace=True)

    data['coffee'] = data['cafetería'] + data['café'] 
    data.drop(columns=['cafetería', 'café'], inplace=True)

    data['drinks'] = data['bar'] + data['barman'] + data['cerveza']  + data['cócteles'] + data['chupito'] + data['mojitos'] + data['queimada']  + data['vermut'] + data['margaritas'] + data['wine']
    data.drop(columns=['bar', 'barman','cerveza', 'cócteles',  'chupito', 'mojitos', 'queimada',  'vermut', 'margaritas'], inplace=True)

    data['meat'] = data['angus'] + data['buey'] + data['butifarra'] + data['cachopo'] + data['carne'] + data['carrilleras'] + data['cecina'] + data['cerdo'] + data['chuleta'] + data['chuletón'] + data['churrasco'] + data['codillo'] + data['cordero'] + data['costillas'] + data['embutidos'] + data['entrecot'] +  data['lechazo'] + data['matadero'] + data['matanza'] + data['mollejas'] + data['morcilla'] + data['oreja']  + data['sobrasada'] + data['solomillo'] + data['t-bone']
    data.drop(columns=['angus', 'buey', 'butifarra', 'cachopo', 'carne', 'carrilleras', 'cecina', 'cerdo', 
                'chuleta', 'chuletón',  'churrasco', 'codillo', 'cordero', 'costillas', 'embutidos', 
                'entrecot',  'lechazo', 'matadero', 'matanza', 'mollejas', 'morcilla', 'oreja', 'sobrasada', 'solomillo',
                't-bone'] , inplace=True)

    data['fish'] = data['atún']  + data['bacalao'] + data['lubina'] + data['mar'] + data['pescadería'] + data['pescado'] + data['sashimi'] + data['trucha']
    data.drop(columns= ['atún','bacalao', 'lubina', 'trucha' ], inplace=True)

    data['seafood'] = data['cangrejo'] + data['calamares'] + data['camarón'] + data['chipirones'] + data['langostinos'] + data['marisco'] + data['mar'] + data['rabas'] + data['zamburiñas']
    data.drop(columns= ['cangrejo', 'calamares','camarón', 'chipirones', 'langostinos', 'marisco', 'rabas', 'zamburiñas' ], inplace=True)


def columnas_sumatorio(data):
# CREAMOS LAS COLUMNAS DE SUMATORIOS
    data['TOTAL_vegano'] = data['vegan'] + data['vegano 1'] + data['vegano 2']
    data['TOTAL_vegetariano'] =  data['vegetarian'] + data['vegetariano 1'] + data['TOTAL_vegano']
    data['TOTAL_sostenible'] = data['sustainable'] + data['sostenible 2']
    data['TOTAL_de_temporada'] = data['seasonal'] + data['frescos 1'] + data['frescos 2'] + data['huerta 1'] + data['huerta 2'] 
    data['TOTAL_orgánico'] = data['organic'] + data['orgánico 1'] + data['orgánico 2']
    data['TOTAL_saludable'] = data['healthy'] + data['saludable 2']
    data['TOTAL_fresco'] = data['seasonal'] + data['TOTAL_de_temporada']
    data['TOTAL_artesano'] = data['handcrafted'] + data['artesano 2']
    data['TOTAL_cero_basura'] = data['zero_waste'] 
    data['TOTAL_de_proximidad'] =  data['proximidad 2']  + data['local 2'] + data['TOTAL_fresco'] 

    return data


def columnas_scoring(data):
# CREAMOS LAS COLUMNAS DE SCORING, QUE SE RELACIONARÁN CON LAS PREFERENCIAS DE USUARIO
    data['SCORE_vegano'] = pd.cut(data['TOTAL_vegano'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_vegetariano'] = pd.cut(data['TOTAL_vegetariano'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_sostenible'] = pd.cut(data['TOTAL_sostenible'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_de_temporada'] = pd.cut(data['TOTAL_de_temporada'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_orgánico'] = pd.cut(data['TOTAL_orgánico'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_saludable'] = pd.cut(data['TOTAL_saludable'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_fresco'] = pd.cut(data['TOTAL_fresco'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_artesano'] = pd.cut(data['TOTAL_artesano'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_cero_basura'] = pd.cut(data['TOTAL_cero_basura'], bins=7, labels=[0,1,2,3,4,5,6])
    data['SCORE_de_proximidad'] = pd.cut(data['TOTAL_de_proximidad'], bins=7, labels=[0,1,2,3,4,5,6])

    return data


def get_recommendations(place_name, index, data, cosine_sim):
    idx = index[place_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:10]
    place_index = [i[0] for i in sim_scores]

    recomendacion = data['place_name'].iloc[place_index]
    
    return recomendacion

def preferencias(ListNum, data):
    cols = ["TOTAL_vegano", "TOTAL_vegetariano", "TOTAL_sostenible", "TOTAL_de_temporada", "TOTAL_orgánico", "TOTAL_saludable", "TOTAL_fresco", "TOTAL_artesano", "TOTAL_cero_basura", "TOTAL_de_proximidad"]
    cercanos = []
    for columna in cols:
        diferencia = data[columna].max() - data[columna].min()
        cercanos.append([])
        indice = cols.index(columna)
        num = ListNum[indice]
        for registro in data[columna]:
            cercanos[indice].append(np.abs(((num*2-1)*0.1)-((registro-data[columna].min()) / diferencia)))
    indices = []
    media = []
    for index in data.index:
        suma_previa = []
        for campo in cercanos:
            suma_previa.append(campo[index])
        media.append((index, np.sum(suma_previa)))
    return [x[0] for x in sorted(media, key= lambda x:x[1])[:10]]