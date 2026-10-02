import pandas as pd #type: ignore
import numpy as np #type: ignore

df = pd.read_csv("transacoes.csv", encoding='latin1')

#Parte 1
print(df["valor"].isnull().sum())

media = df.groupby("estado_cliente")["valor"].mean()
print(media)
df["valor"] = df["valor"].fillna(df.groupby('estado_cliente')['valor'].transform('median'))

print(df)
print(df["valor"].isnull().sum())

df['plataforma'] = 'Mobile'

#Parte 2

df['data_transacao'] = pd.to_datetime(df['data_transacao'])
df['data_transacao'] = df['data_transacao'].dt.tz_localize('America/Sao_Paulo')

df['dia'] = df['data_transacao'].dt.day_name()
df['mes'] = df['data_transacao'].dt.month

df = df.drop_duplicates(keep='first')

print(df)
#Parte 3

df_filtro_query = df.query('(estado_cliente == "SP" | estado_cliente == "RJ") & valor > 5000').sort_values(by='estado_cliente')
df_filtro = (
    ((df["estado_cliente"] == "SP") |
    (df["estado_cliente"] == "RJ")) &
    (df["valor"] > 5000)
)



print(df_filtro_query)
print(df[df_filtro].copy())

#Parte 4

risco = {
    'C100': 'Baixo',
    'C101': 'Alto',
    'C102': 'Médio',
    'C103': 'Médio',
    'C104': 'Baixo'
}

df['risco'] = df['id_cliente'].map(risco)
print(df['risco'])

print(df.dtypes)

df_pivotada = df.pivot_table( values="valor", index=['mes'], columns=["risco"], aggfunc='sum', margins=True )
print(df_pivotada)

#Parte 5

df['z_score'] = df.groupby('estado_cliente')['valor'].transform(lambda x: (x - x.mean()) / x.std())
print(df)

z_rule = (df['z_score'] > 2.5)

df_z_filtro = df[z_rule].copy
print("Possíveis frauds: \n", df_z_filtro)

#Parte 6