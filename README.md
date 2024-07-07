Este projeto tem como objetivo aplicar algoritmos de agrupamento em uma base de dados composta por 777 registros e 18 variáveis, a fim de segmentar universidades em públicas e privadas com base em suas características. Avaliamos o desempenho de três modelos de agrupamento: K-Means, DBSCAN e Agrupamento Hierárquico.

### Algoritmos Utilizados

- **K-Means**: Particiona os dados em k grupos onde cada observação pertence ao grupo com a média mais próxima.
- **DBSCAN**: Algoritmo baseado em densidade, que identifica clusters de diferentes formas e tamanhos sem necessidade de especificar o número de clusters.
- **Agrupamento Hierárquico**: Constrói uma hierarquia de clusters, fundindo iterativamente os clusters mais próximos.

### Análise dos Dados

A análise revelou que existem mais instituições privadas do que públicas na base de dados, com um total de 526 privadas contra 212 públicas.

![image](https://github.com/IsadoraPrevitalle/Agrupamento_Instituicao/assets/104457205/89bfbb86-b698-4334-85eb-ad224ba6d4f4)

### Pré-Processamento

Realizamos o pré-processamento dos dados, incluindo análise de médias, desvio padrão, validação de valores nulos, verificação dos quartis e normalização dos dados. Este passo foi essencial para garantir a qualidade dos dados antes de aplicar os algoritmos de agrupamento.

![image](https://github.com/IsadoraPrevitalle/Agrupamento_Instituicao/assets/104457205/ad0f3d7b-50fa-42ae-b49e-7a8518cf5ddd)


## Resultados

### K-Means

- **Clusters**: 2

# Dados Originais:

![image](https://github.com/IsadoraPrevitalle/Agrupamento_Instituicao/assets/104457205/c416730b-26ed-43ec-accc-a7703662e1a7)

# Dados Previstos:

![image](https://github.com/IsadoraPrevitalle/Agrupamento_Instituicao/assets/104457205/3675c60c-e69f-49e4-8de1-03e337599167)


### DBSCAN

- **Raio**: 0.5

# Dados Originais:

![image](https://github.com/IsadoraPrevitalle/Agrupamento_Instituicao/assets/104457205/20263b06-97d1-4e01-8824-78086965e0b2)

# Dados Previstos:

![image](https://github.com/IsadoraPrevitalle/Agrupamento_Instituicao/assets/104457205/0c3cf9e7-752a-438d-a2e7-5bb1560abf2a)


### Agrupamento Hierárquico

- **Clusters**: 2

![image](https://github.com/IsadoraPrevitalle/Agrupamento_Instituicao/assets/104457205/84d20000-bfdc-42c6-bc60-8706be5f7de6)

