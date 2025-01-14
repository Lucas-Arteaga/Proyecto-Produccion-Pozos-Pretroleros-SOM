import pandas as pd
import matplotlib.pyplot as plt

df_produccion = pd.read_csv("produccin-de-pozos-de-gas-y-petrleo-2023.csv", low_memory=False)

""" print(df_produccion.columns) """

data = df_produccion[['anio', 'mes', 'idpozo', 'prod_pet', 'prod_gas', 'prod_agua', 'tipoestado','tipopozo', 'empresa', 'formacion', 
'areapermisoconcesion','areayacimiento', 'cuenca', 'provincia', "tipo_de_recurso"]]
print(data['tipoestado'].unique())
""" for columna in data:
  print(columna)
  print(data[columna].unique())
  print("---------------------------------------------------------------")"""

new_data = data[
    (data['tipoestado'].isin(['Extracción Efectiva', 'Abandonado'])) & 
    (data['tipo_de_recurso'].isin(['CONVENCIONAL', 'NO CONVENCIONAL'])) &
    (data['tipopozo'].isin(['Petrolífero', 'Gasífero'])) &
    (~data['areayacimiento'].isin(['POZOS SIN YACIMIENTO', 'SIN NOMBRE', 'PUESTO SIN NOMBRE'])) &
    (data['prod_pet'] >= 0) &
    (data['prod_gas'] >= 0) &
    (data['prod_agua'] >= 0)
]

db_nulos = new_data.dropna() #limpia los valores faltantes
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
""" db_pga = db_prov[(db_prov['prod_pet'] < 350) & (db_prov['prod_gas'] < 420) & (db_prov['prod_agua'] < 4700)]  """

print(db_prov['prod_pet'].quantile(0.95))
print(db_prov['prod_gas'].quantile(0.95))
print(db_prov['prod_agua'].quantile(0.95))

""" #-------------------------------------------------------------------------

#defino el rengo de produccion de petroleo
bins_p = [0, p95/3, 2*(p95/3), p95]
bins_g = [0, g95/3, 2*(g95/3), g95]
bins_a = [0, a95/3, 2*(a95/3), a95]
# Definir las etiquetas para cada categoría
labels = ['baja', 'media', 'alta']
db_pga = db_prov[(db_prov['prod_pet'] < p95) & (db_prov['prod_gas'] < g95) & (db_prov['prod_agua'] < a95)] 
# Crear una nueva columna 'categoria_prod' basada en los valores de 'prod_pet'
db_pga['rango_p'] = pd.cut(db_pga['prod_pet'], bins=bins_p, labels=labels, right=False)
db_pga['rango_g'] = pd.cut(db_pga['prod_gas'], bins=bins_g, labels=labels, right=False)
db_pga['rango_a'] = pd.cut(db_pga['prod_agua'], bins=bins_a, labels=labels, right=False)

print(db_pga[['rango_a', 'rango_p', 'rango_a', 'prod_pet', 'prod_gas','prod_agua']].sample(20)) """
#Exportar el DataFrame 
""" db_pga.to_csv('DatasetInformeFinal.csv', index=False) """
