import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Carregar a base de dados
df = pd.read_csv('Data_College_normalizada.csv')

# Transformação da classe meta
df['Private'] = df['Private'].replace({'No': 1, 'Yes': 0})

# Visualizar as primeiras linhas e estatísticas descritivas
print(df.head())
print(df.describe())

# Construir uma matriz contendo todos os atributos com exceção da class
X = df.drop(['University_name', 'Private'], axis=1)  # Remover colunas não numéricas

# Inicializar KMeans com o número desejado de clusters
kmeans = KMeans(n_clusters=2)
#kmeans = KMeans(n_clusters=2, init='k-means++') #Testando com k-means++ para verificar acurácia -> acurácia menor 0.459

# Treinar o algoritmo
kmeans.fit(X)

# Imprimir os centroides
print('Centroids:')
print(kmeans.cluster_centers_)

# Imprimir os rótulos atribuídos a cada amostra
print('Labels:')
print(kmeans.labels_)

# Adicionar os rótulos dos clusters ao DataFrame original
df['cluster'] = kmeans.labels_

# Visualizar os resultados
sns.scatterplot(data=df, x='Top10perc', y='Top25perc', hue='cluster')
plt.scatter(kmeans.cluster_centers_[:, 5], kmeans.cluster_centers_[:, 6], s=100, c='black')  # Coordenadas dos centroides
plt.show()

sns.scatterplot(data=df, x='Top10perc', y='Top25perc', hue='Private')
plt.show()

# Visualizar a distribuição da quantidade de grupos
distancia = {}
for k in range(1, 15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    distancia[k] = kmeans.inertia_

sns.pointplot(x=list(distancia.keys()), y=list(distancia.values()))
plt.xlabel('Número de clusters (k)')
plt.ylabel('Distorção')
plt.title('Elbow Method')
plt.show()

print(df)
acuracia = accuracy_score(df['cluster'], df['Private'])

print("Acurácia do KMeans em relação à coluna binária:", acuracia)

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