import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

db_crudo = pd.read_csv("datasetProduccion2023.csv")

db_nulos = db_crudo.dropna() #limpia los valores faltantes
db_prov = db_nulos[(db_nulos['provincia'] != 'Estado Nacional')]

db_prov['trimestre'] = pd.cut(db_prov['mes'], bins=[0, 3, 6, 9, 12], labels=[1, 2, 3, 4], right=True) #agrega la seccion trimestres

provincia_dict = {
    'Mendoza': 'centro',
    'Neuquén': 'centro',
    'La Pampa': 'centro',
    'Salta': 'norte',
    'Jujuy': 'norte',
    'Formosa': 'norte',
    'Tierra del Fuego': 'sur',
    'Santa Cruz': 'sur',
    'Chubut': 'sur',
    'Rio Negro': 'sur'
}
db_prov['region'] = db_prov['provincia'].map(provincia_dict) #agrega la seccion region

#nos dimos cuenta que el percentil 95 da de produccion de petroleo 350
db_pga = db_prov[(db_prov['prod_pet'] < 350) & (db_prov['prod_gas'] < 420) & (db_prov['prod_agua'] < 4700)] 

#defino el rengo de produccion de petroleo
bins_p = [0, 350/3, 700/3, 350]
# Definir las etiquetas para cada categoría
labels = ['baja', 'media', 'alta']
# Crear una nueva columna 'categoria_prod' basada en los valores de 'prod_pet'
db_pga['rango_p'] = pd.cut(db_pga['prod_pet'], bins=bins_p, labels=labels, right=False)


bins_g = [0, 420/3 , 840/3, 420]
bins_a = [0, 4700/3 , 9400/3, 4700]

db_pga['rango_g'] = pd.cut(db_pga['prod_gas'], bins=bins_g, labels=labels, right=False)
db_pga['rango_a'] = pd.cut(db_pga['prod_agua'], bins=bins_a, labels=labels, right=False)

""" db_pga.to_csv("datasetCategorizado.csv", index=False) """

""" print(db_pga.sample(15)) """