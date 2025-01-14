import pandas as pd
import matplotlib.pyplot as plt

#CAPITULO 4
df_produccion = pd.read_csv("DatasetInformeFinal.csv", low_memory=False)

""" print("Columnas")
print(df_produccion.columns)
print("info")
print(df_produccion.info())
print("describe")
print(df_produccion.describe())
print("sample")
print(df_produccion.sample(20))

print(df_produccion["tipoestado"].unique())
print(df_produccion["areayacimiento"].unique())
print(df_produccion["clasificacion"].unique())
print(df_produccion["proyecto"].unique())


datos_pozo = df_produccion[df_produccion['idpozo'] == 153019]
print(datos_pozo.head(20)) """
""" print(df_produccion[df_produccion["clasificacion"] == "EXPLOTACION"]["subclasificacion"].unique()) """

""" empresas = df_produccion.groupby("empresa").size().sort_values(ascending=False)
empresas.plot(kind = "bar")
plt.show()
"""


#PIPELINE INJURIES
""" df_injuries = pd.read_csv("PipelinInjuries.csv")

print("Columnas")
print(df_injuries.columns)
print("info")
print(df_injuries.info())
print("describe")
print(df_injuries.describe())
print("sample")
print(df_injuries.sample(20))

print("Cause Category")
print(df_injuries["Cause Category"].unique())
print("Cause Subcategory")
print(df_injuries["Cause Subcategory"].unique())
print("Pipeline Type")
print(df_injuries["Pipeline Type"].unique()) """



#FORCE 2020
""" df_geodata = pd.read_csv("Force2020.csv",delimiter=";")

print("Columnas")
print(df_geodata.columns)
print("info")
print(df_geodata.info())
print("describe")
print(df_geodata.describe())
print("sample")
print(df_geodata.sample(20)) """

#quiero remover columnas de mi dataset
df_produccion = df_produccion.drop(columns=['areapermisoconcesion', 'areayacimiento', 'idpozo', 'empresa'])
#quiero sacar los valores nan de rango_a
df_produccion = df_produccion.dropna(subset=['rango_a'])
print(df_produccion.describe)

