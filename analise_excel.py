#Importando a biblioteca Pandas
import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("D:/Area Trabalho ate 17-01-2022/Cursos/Geração Tech UNIMED-BH - Ciencia de Dados/Python/Python_Pandas_Dio-master/datasets/Aracaju.xlsx")
df2 = pd.read_excel("D:/Area Trabalho ate 17-01-2022/Cursos/Geração Tech UNIMED-BH - Ciencia de Dados/Python/Python_Pandas_Dio-master/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("D:/Area Trabalho ate 17-01-2022/Cursos/Geração Tech UNIMED-BH - Ciencia de Dados/Python/Python_Pandas_Dio-master/datasets/Natal.xlsx")
df4 = pd.read_excel("D:/Area Trabalho ate 17-01-2022/Cursos/Geração Tech UNIMED-BH - Ciencia de Dados/Python/Python_Pandas_Dio-master/datasets/Recife.xlsx")
df5 = pd.read_excel("D:/Area Trabalho ate 17-01-2022/Cursos/Geração Tech UNIMED-BH - Ciencia de Dados/Python/Python_Pandas_Dio-master/datasets/Fortaleza.xlsx")

#Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

#Exibindo as 5 primeiras linhas
print (df.head())

#Exibindo as 5 últimas linhas
print (df.tail())

#Exibindo 5 linhas de amostra
print (df.sample(5))

#Verificando o tipo de dado de cada coluna
print (df.dtypes)

#Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")

#Verificando alteração do tipo de dado da coluna LojaID
print (df.dtypes)

#Tratando valores faltantes

#Consultando linhas com valores faltantes
print (df.isnull().sum())

#Substituindo valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean, inplace=True)

print (df.isnull().sum())

#Substituindo valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

#Apagando linhas com valores nulos
df.dropna(inplace=True)

#Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

#Apagando as linhas com valores nulos em todas as colunas
df.dropna(how="all", inplace=True)

#Criando novas colunas

#Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])

print(df.head())

#Retornando a maior receita
print (df["Receita"].max())

#Retornando a menor receita
print (df["Receita"].min())

#nlargest (retornar top 3 com base na coluna receita)
print (df.nlargest(3, "Receita"))

#nsmallest (retornar top 3 com base na coluna receita)
print (df.nsmallest(3, "Receita"))

#Agrupamento por cidade (soma da receita por cidade)
print (df.groupby("Cidade")["Receita"].sum())

#Ordenando o conjunto de dados
print (df.sort_values("Receita", ascending=False).head(10))

#Trabalhando com Datas

#Transformando a coluna de data em tipo inteiro
df["Data"] = df ["Data"].astype("int64")

print(df.dtypes)

#Transformando a coluna de data em tipo data
df["Data"] = pd.to_datetime(df["Data"])

print(df.dtypes)

#Agrupando por ano
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

#Criando uma nova coluna com o ano
df["Ano_Venda"] = df ["Data"].dt.year

print (df.sample(5))

#Extraindo o mês e o dia
df["mes_venda"], df ["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

print (df.sample(5))

#Retornando a data mais antiga
print (df["Data"].min())

#Calculando a diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()

print (df.sample(5))

#Criando coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

print (df.sample(5))

#Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

print (vendas_marco_19.sample(20))