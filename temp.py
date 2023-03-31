import pandas as pd

df = pd.read_csv("solicitudes_credito.csv", sep=";")
df.rename(columns={'Unnamed: 0':'index'},inplace=True)
df.set_index('index',inplace=True)

df.sexo = df.sexo.str.lower().astype(str).str.strip()
df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.capitalize().str.strip()
df.idea_negocio = df.idea_negocio.str.replace('-',' ', regex=False).str.replace('_',' ', regex=False).str.capitalize().str.strip()
df.barrio = df.barrio.str.replace('-',' ', regex=False).str.replace('_',' ', regex=False).str.capitalize().str.strip()
df.estrato = df.estrato.astype("str").str.capitalize()
df.comuna_ciudadano = df.comuna_ciudadano.astype(str).str.capitalize()
df.fecha_de_beneficio = pd.to_datetime(df["fecha_de_beneficio"], dayfirst = True)
df.monto_del_credito = df.monto_del_credito.str.replace(",","",regex=True).str.replace("$","",regex=True).str.strip()
df.monto_del_credito = df.monto_del_credito.astype(float)
df.línea_credito=df.línea_credito.str.replace('-',' ', regex=False).str.replace('_',' ', regex=False).str.capitalize().str.strip()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print(df.línea_credito.value_counts())
