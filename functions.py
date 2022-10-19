# from difflib import SequenceMatcher
import pandas as pd
import numpy as np


# def unifica_columnas(data):
# # UNIFICAMOS COLUMNAS CON PLURALES O GÉNEROS DISTINTOS
#     data_dict = {"nombre_data1":[],"nombre_data2":[],"ratio":[]}
#     for x in data.iloc[::,18:].columns:
#         for y in data.iloc[::,18:].columns:
#             ratio = SequenceMatcher(None, y, x).ratio() 
#             data_dict["nombre_data1"].append(x)
#             data_dict["nombre_data2"].append(y)
#             data_dict["ratio"].append(ratio)

#     data_ratio = pd.DataFrame(data_dict)
#     resumen = data_ratio[(data_ratio['ratio']>0.84)&(data_ratio['ratio']<1)].sort_values(by='ratio', ascending=False).head(500)


#     for x in range(len(resumen)):
#         try:
#             data[resumen.iloc[x]["nombre_data1"]] = data[resumen.iloc[x]["nombre_data1"]] + data[resumen.iloc[x]["nombre_data2"]]
#             data.drop(columns = resumen.iloc[x]["nombre_data2"], inplace=True)
#         except:
#             continue
    
#     return data


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
    data['vegan'] = data['vegana'] + data['crudiveganismo'] + data['crueldad'] + data['heura'] + data['leche vegetal'] 
    data.drop(columns=['vegana', 'crudiveganismo', 'crueldad', 'heura', 'leche vegetal'], inplace=True)

    data['vegetarian'] = data['vegan'] + data['vegetales']
    data.drop(columns = ['vegan', 'vegetales'])

    data['healthy'] = data['alimentación sana'] + data['comer sano'] + data['comida saludable'] + data['comida sana'] + data['salud'] + data['sano'] + data['slow food'] + data[ 'smoothies'] + data['integral']  + data['saludable 2']
    data.drop(columns=['alimentación sana', 'comer sano', 'comida saludable',
                    'comida sana', 'salud', 'sano', 'slow food', 'smoothies', 'integral'], inplace=True)

    data['seasonal'] = data['temporada'] + data['productos frescos'] + data['huerto'] + data['granja'] + data['verdura fresca']
    data.drop(columns=['temporada', 'productos frescos', 'huerto', 'granja', 'verdura fresca'], inplace=True)

    data['sustainable'] = + data['eficiente'] + data['justa'] +  data['cooperativa'] + data['ética'] + data['agricultores'] + data['planeta'] + data['respetuoso con el medio ambiente'] 
    data.drop(columns=['eficiente', 'justa', 'cooperativa', 'ética', 'agricultores', 'planeta', 'respetuoso con el medio ambiente'], inplace=True)

    data['handcrafted'] = data['artesanal']  + data['cervezas artesanas'] + data['tradicional'] + data['tradición']
    data.drop(columns=['artesanal', 'tradicional', 'tradición'], inplace=True)

    data['organic'] = data['productos orgánicos'] 
    data.drop(columns=['productos orgánicos'], inplace=True)

    data['zero_waste'] = data['cero basura'] + data['reciclados'] + data['reciclaje'] + data['reciclar'] + data['a granel'] + data['biodegradables'] + data['too good to go']
    data.drop(columns=['cero basura','reciclados','reciclaje','reciclar', 'a granel', 'biodegradables', 'too good to go'], inplace=True)

    data['alergens'] = data['alérgenos'] + data['gluten'] + data['sin gluten'] + data['pan sin gluten'] + data['lactosa'] + data['celíacos']
    data.drop(columns=['alérgenos', 'gluten', 'sin gluten', 'lactosa', 'celíacos'], inplace=True)

    data['wine'] = data['vino'] + data['vinos naturales'] + data['maridaje'] + data['tinto de verano'] 
    data.drop(columns=['vino', 'vinos naturales', 'maridaje', 'tinto de verano'], inplace=True)

    data['bread'] = data['pan sin gluten'] + data['obrador'] + data['palmera'] + data['palmeritas'] + data['bollería'] + data['horno'] + data['masa'] + data['masa madre']
    data.drop(columns=['pan sin gluten','obrador','palmera', 'palmeritas', 'bollería', 'horno', 'masa', 'masa madre'], inplace=True)

    data['coffee'] = data['cafetería'] + data['café'] + data['café con leche'] + data['flat white']
    data.drop(columns=['cafetería', 'café', 'café con leche', 'flat white'], inplace=True)

    data['drinks'] = data['bar'] + data['barman'] + data['cervezas'] + data['cervezas artesanas'] + data['cócteles'] + data['estrella galicia'] + data['chupito'] + data['mojitos'] + data['queimada'] + data['sangria'] + data['vermut'] + data['margaritas'] + data['wine']
    data.drop(columns=['bar', 'barman','cervezas', 'cervezas artesanas','cócteles', 'estrella galicia', 'chupito', 'mojitos', 'queimada', 'sangria', 'vermut', 'margaritas'], inplace=True)

    data['meat'] = data['angus'] + data['buey'] + data['butifarra'] + data['cachopo'] + data['carne'] + data['carne de oveja'] + data['carne de oveja'] + data['carrilleras'] + data['cecina'] + data['cerdo'] + data['chuleta'] + data['chuletón'] + data['chuletón de ávila'] + data['churrasco'] + data['codillo'] + data['cordero'] + data['costillas'] + data['costillas de cerdo'] + data['embutidos'] + data['entrecot'] + data['hot dog'] + data['lechazo'] + data['matadero'] + data['matanza'] + data['mollejas'] + data['morcilla'] + data['oreja'] + data['rabo de toro'] + data['sobrasada'] + data['solomillo'] + data['steak tartar'] + data['t-bone']
    data.drop(columns=['angus', 'buey', 'butifarra', 'cachopo', 'carne', 'carne de oveja', 'carne de oveja', 'carrilleras', 'cecina', 'cerdo', 
                    'chuleta', 'chuletón', 'chuletón de ávila', 'churrasco', 'codillo', 'cordero', 'costillas', 'costillas de cerdo', 'embutidos', 
                    'entrecot', 'hot dog', 'lechazo', 'matadero', 'matanza', 'mollejas', 'morcilla', 'oreja', 'rabo de toro', 'sobrasada', 'solomillo',
                    't-bone'] , inplace=True)

    data['fish'] = data['atún'] + data['atún rojo'] + data['bacalao'] + data['lubina'] + data['mar'] + data['pescadería'] + data['pescado'] + data['sashimi'] + data['trucha']
    data.drop(columns= ['atún', 'atún rojo','bacalao', 'lubina', 'trucha' ], inplace=True)

    data['seafood'] = data['cangrejo'] + data['calamares'] + data['camarón'] + data['chipirones'] + data['langostinos'] + data['marisco'] + data['mar'] + data['rabas'] + data['zamburiñas']
    data.drop(columns= ['cangrejo', 'calamares','camarón', 'chipirones', 'langostinos', 'marisco', 'rabas', 'zamburiñas' ], inplace=True)

    data['chicken'] = data['pollo'] + data['pollo a la brasa'] + data['pollo al ast'] + data['pollo asado']
    data.drop(columns= ['pollo', 'pollo a la brasa', 'pollo al ast', 'pollo asado'], inplace=True)

    return data


def columnas_sumatorio(data):
# CREAMOS LAS COLUMNAS DE SUMATORIOS
    data['TOTAL_vegano'] = data['vegan'] + data['vegano 1'] 
    data['TOTAL_vegetariano'] =  data['vegetarian'] + data['vegetariano 1']
    data['TOTAL_sostenible'] = data['sustainable'] + data['sostenible 2']
    data['TOTAL_de_temporada'] = data['seasonal'] 
    data['TOTAL_orgánico'] = data['organic']
    data['TOTAL_saludable'] = data['healthy']+ data['saludable 2']
    data['TOTAL_fresco'] = data['seasonal'] + data['frescos 1'] + data['huerta 2']
    data['TOTAL_artesano'] = data['handcrafted'] + data['artesano 2']
    data['TOTAL_cero_basura'] = data['zero_waste'] 
    data['TOTAL_de_proximidad'] =  data['proximidad 2']

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
    return data['place_name'].iloc[place_index]