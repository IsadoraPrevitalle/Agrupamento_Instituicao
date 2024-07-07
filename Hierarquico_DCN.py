import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Carregar a base de dados
df = pd.read_csv('Data_College_normalizada.csv')

# Transformação da classe meta
df['Private'] = df['Private'].replace({'No': 1, 'Yes': 0})

# Visualizar as primeiras linhas e estatísticas descritivas
print(df.head())
print(df.describe())

# Construir uma matriz contendo todos os atributos com exceção da class
x = df.drop(['University_name', 'Private'], axis=1)  # Remover colunas não numéricas

print(x)

z = linkage(x, method='ward')
plt.figure(figsize=(12, 5))
dendrogram(z)
plt.title('Dendograma')
plt.xlabel('Amostras')
plt.ylabel('Distância')
plt.axhline(y=10, color='r', linestyle='--')
plt.show()

#executar o agrupamento hierarquico
agg__clustering = AgglomerativeClustering(n_clusters=2) 

#agg__clustering = AgglomerativeClustering #Testando cluster por default 
rotulos = agg__clustering.fit_predict(x)
df['cluster'] = rotulos

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