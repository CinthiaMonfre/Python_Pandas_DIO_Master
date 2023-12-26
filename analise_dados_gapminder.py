#importanto a biblioteca pandas
import pandas as pd

df = pd.read_csv ("D:/Area Trabalho ate 17-01-2022/Cursos/Geração Tech UNIMED-BH - Ciencia de Dados/Python/Python_Pandas_Dio-master/datasets/Gapminder.csv", on_bad_lines='skip', sep=";")

df = df.rename(columns={"country": "País", "continent": "Continente", "year": "Ano", "lifeExp": "ExpcVida", "pop": "População", "gdpPercap": "PIB"})

print (df.head(15))

#total de linhas e colunas
df.shape
print (df.shape)

#mostrar somente colunas
print(df.columns)

#mostrar tipos de dados
print (df.dtypes)

#monstrar 15 últimas linhas
print(df.tail(15))

#dados estatísticos (total de linhas, média, desvio padrão, valor mínino, quartis 25%, 50%, 75% e valor máximo)
print(df.describe())

#mostrar valores únicos da coluna Continente
print(df["Continente"].unique())

#localizar e filtrar linhas com continente "oceania"
Oceania_df = df[df["Continente"] == "Oceania"]

print(Oceania_df.head())

#agrupar dados (quantos países por continente )
print(df.groupby("Continente")["País"].nunique())

#agrupar dados (quais países por continente )
print(df.groupby("Continente")["País"].unique())

#agrupar dados (qual a expectativa de vida média para cada ano)
print(df.groupby("Ano")["ExpcVida"].mean())

#somar coluna PIB
print (df["PIB"].sum())