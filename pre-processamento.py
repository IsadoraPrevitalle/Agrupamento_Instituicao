import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('Data_College.csv')

print(df)
df.rename(columns={'Unnamed: 0': 'University_name'}, inplace=True)
print(df)

#Dados descritivos do DataFrame
print(df.describe())

#Diferentes valores da classe private 
print(np.unique(df['Private'], return_counts = True))

# Tratamento de valores faltantes
# Somatória nulos
print(df.isnull().sum())

#Visualização dos dados
#Histogramas de algumas das classes principais

#Histograma da Classe meta
sn.countplot(x=df['Private'])
plt.show()

#Histograma da taxa de graduação
sn.countplot(x=df['Grad.Rate'])
plt.show()

#Histograma da taxa de estudantes na faculdade
sn.countplot(x=df['S.F.Ratio'])
plt.show()

#Normalização dos dados:
Colunas = df.columns[2:]  #Ignorando as duas primeiras colunas 'University_name' e 'Private' por não serem numéricas

# Normalização Min-Max
for col in Colunas:
    min_val = df[col].min()
    max_val = df[col].max()
    df[col] = (df[col] - min_val) / (max_val - min_val)

# Salvando a base de dados normalizada
# df.to_csv('Data_College_normalizada.csv', index=False)

df_nomalizada = pd.read_csv('Data_College_normalizada.csv')
print(df_nomalizada)
print(df_nomalizada.describe())


df = df.drop(['University_name'], axis=1)
# Calcular as médias de cada atributo para cada cluster
media_meta = df.groupby('Private').mean()

# Calcular a diferença entre as médias de cada atributo para cada par de clusters
cluster_diff = media_meta.diff().abs().fillna(0)

# Encontrar os atributos com maiores diferenças médias entre os clusters
important_features = cluster_diff.idxmax()
print("Colunas mais impactantes na classificação do cluster:")
print(important_features)