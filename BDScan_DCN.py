import pandas as pd
import seaborn as sns
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Carregar a base de dados
df = pd.read_csv('Data_College_normalizada.csv')

# Transformação da classe meta
df['Private'] = df['Private'].replace({'No': -1, 'Yes': 0})

#Criando visualização
sns.set(rc ={'figure.figsize':(10,5)})
sns.scatterplot(data=df, x='Top10perc', y='Top25perc', hue='Private')
plt.show()

# Construir uma matriz contendo todos os atributos com exceção da class
x = df.drop(['University_name', 'Private'], axis=1)  # Remover colunas não numéricas

#Criando e treinando modelo
DBScan = DBSCAN(eps=0.5)
DBScan.fit(x)

#Obtendo os rótulos dos grupos
rotulos = DBScan.labels_
print(rotulos)
df['cluster'] = rotulos
print(df)

#Plotando grafico
sns.scatterplot(data=df, x='Top10perc', y='Top25perc', hue='cluster')
plt.show()


print(df)
acuracia = accuracy_score(df['cluster'], df['Private'])

print("Acurácia ", acuracia)

# Calcular a matriz de confusão
matriz_confusao = confusion_matrix(df['cluster'], df['Private'])
print("Matriz de confusão:")
print(matriz_confusao)

#Exibe as métricas de avaliação
print(classification_report(df['cluster'], df['Private']))

# Exibir o gráfico da matriz de confusão usando seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(matriz_confusao, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Matriz de Confusão")
plt.show()