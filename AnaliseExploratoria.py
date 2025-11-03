import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração para melhor visualização dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Carregar os Dados
df = pd.read_csv('dados_jogadores_sinteticos.csv')
print("--- PRIMEIRAS 5 LINHAS ---")
print(df.head())

# Limpeza e pré-processamento inicial dos dados

print("\n--- INFORMAÇÕES GERAIS E TIPOS DE DADOS ---")
df.info()

print("\n--- VERIFICANDO VALORES NULOS (AUSENTES) ---")
print(df.isnull().sum())

# Pré-processamento: Criação de uma 'Feature' de Razão
# Razão entre Gasto e Engajamento.
df['Gasto_Por_Hora'] = df['Gasto_Total_BRL'] / df['Tempo_Jogado_Horas']
df['Gasto_Por_Hora'].replace([np.inf, -np.inf], 0, inplace=True) # Trata divisões por zero ou infinitas

print("\n--- ANÁLISE DE GASTO POR HORA (NOVA FEATURE) ---")
print(df['Gasto_Por_Hora'].describe())

# 2 Análise descritiva dos dados (distribuição, tendências e padrões)
# A. Análise de variável alvo (comprou_oferta_x)
taxa_conversao = df['COMPROU_OFERTA_X'].mean() * 100

print(f"\n--- TAXA DE CONVERSÃO DA OFERTA X ---")
print(f"Taxa de Conversão Simulada: {taxa_conversao:.2f}%")

# Gráfico da Distribuição da Variável Alvo
plt.figure(figsize=(6, 4))
sns.countplot(x='COMPROU_OFERTA_X', data=df)
plt.title('Distribuição da Variável Alvo (Comprou Oferta X)')
plt.xlabel('Comprou (1) / Não Comprou (0)')
plt.ylabel('Contagem de Jogadores')
plt.show()

# B. Análise da distribuição de gastos (regra 80/20)
print("\n--- ESTATÍSTICAS DESCRITIVAS DE GASTO ---")
print(df['Gasto_Total_BRL'].describe(percentiles=[.90, .95, .99]))

# Confirmação visual da cauda longa (Baleias)
plt.figure(figsize=(10, 5))
sns.histplot(df[df['Gasto_Total_BRL'] > 0]['Gasto_Total_BRL'], bins=50, kde=True)
plt.title('Distribuição de Gastos (Apenas Jogadores Pagantes)')
plt.xlabel('Gasto Total (BRL)')
plt.ylabel('Frequência')
plt.xlim(0, df['Gasto_Total_BRL'].quantile(0.99)) # Limita o eixo X para melhor visualização
plt.show()

# Insight: A maioria dos gastos se concentra em valores baixos, mas os percentis 95/99 indicam a presença de 'Baleias'.

# C. Engajamento vs. Compra
# Comparação do Nível entre Pagantes e Não Pagantes
plt.figure(figsize=(10, 5))
sns.boxplot(x='COMPROU_OFERTA_X', y='Nivel_Atual', data=df)
plt.title('Nível Atual por Status de Compra da Oferta X')
plt.xlabel('Comprou Oferta X (0=Não, 1=Sim)')
plt.ylabel('Nível Atual')
plt.show()

# Insight: Se o boxplot de '1' for visivelmente mais alto, indica que o Nível é um bom preditor.

# 3. Identificação de variáveis importantes e correlações

# Seleciona as colunas numéricas (excluindo o ID)
colunas_numericas = df.drop(columns=['ID_Jogador']).columns

# Calcula a Matriz de Correlação
matriz_correlacao = df[colunas_numericas].corr()

print("\n--- MATRIZ DE CORRELAÇÃO com a Variável Alvo ---")
# Filtra apenas a correlação com a variável alvo para uma visão rápida
correlacao_alvo = matriz_correlacao['COMPROU_OFERTA_X'].sort_values(ascending=False)
print(correlacao_alvo)

# Visualização da Matriz de Correlação (Heatmap)
plt.figure(figsize=(8, 7))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlação entre Variáveis')
plt.show()