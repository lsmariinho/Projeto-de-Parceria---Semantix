# Projeto de Parceria Ebac e Semantix
Projeto do Curso Análista de Dados

Dashboard: https://lookerstudio.google.com/reporting/f926b5f9-c6fa-4b14-98fa-759dad1da41b

Este projeto de Análise de Dados aborda a problemática central da monetização em jogos Free-to-Play (F2P): a baixa taxa de conversão de ofertas genéricas. O objetivo é demonstrar uma metodologia robusta para aumentar o Valor do Tempo de Vida (LTV) do jogador.

Metodologia:

* **Dados: Utilização de dados sintéticos gerados via Python, simulando a estrutura econômica real (Regra 80/20 e propensão a gastar).
* **Análise: Execução de Análise Exploratória de Dados (EDA) para identificar os preditores mais fortes: Histórico de Gasto e Nível de Progresso.
* **Solução: Desenvolvimento de um plano estratégico baseado na segmentação e otimização de timing da oferta, provando que o foco deve ser no upsell e em jogadores de alto engajamento.


## 1. Coleta e Geração de Dados

### 1.1. Natureza da Fonte de Dados
Devido à confidencialidade das informações transacionais em jogos Free-to-Play (F2P), este projeto utiliza **Dados Sintéticos** como metodologia de **Prova de Conceito (PoC)**. O objetivo é demonstrar a capacidade de aplicar técnicas robustas de análise e modelagem preditiva em um cenário que simula a realidade do mercado.

### 1.2. Metodologia de Geração
O dataset (`dados_jogadores_sinteticos.csv`), com 5000 registros, foi gerado via **Script Python** (utilizando Pandas e NumPy) e espelha as seguintes premissas de negócio:

* **Regra 80/20 (Estrutura de Gasto):** A coluna `Gasto_Total_BRL` seguiu uma Distribuição Lognormal, simulando que apenas ~15% dos jogadores são pagantes e que uma minoria (as "Baleias") gera a maior parte da receita.
* **Propensão a Gastar:** A variável alvo (`COMPROU_OFERTA_X`) foi correlacionada com variáveis de engajamento (`Nivel_Atual`, `Gasto_Total_BRL`), garantindo que a análise encontre relações preditivas válidas.

### 1.3. Variáveis Chave do Dataset
O dataset contém variáveis essenciais para a segmentação e predição: `ID_Jogador`, `Dias_Desde_Instalacao`, `Nivel_Atual`, `Tempo_Jogado_Horas`, `Gasto_Total_BRL` e a variável alvo binária `COMPROU_OFERTA_X` (Comprou a Oferta X: 0 ou 1).

## 2. Modelagem (Análise Exploratória e Predição)

A fase de modelagem foi iniciada com a **Análise Exploratória de Dados (EDA)**, essencial para traduzir o comportamento simulado em insights acionáveis, preparando o terreno para um futuro modelo preditivo (Regressão Logística/Classificação).

### 2.1. Objetivos da Modelagem
O objetivo principal foi identificar quais variáveis de comportamento (features) são os preditores mais fortes para a variável alvo, com foco em:
1.  Quantificar a ineficiência da oferta genérica (KPI: Taxa de Conversão).
2.  Provar o poder preditivo do Histórico de Gasto.
3.  Identificar o timing ideal (Nível de Progresso) para a exibição da oferta.

### 2.2. Insights Encontrados (Base para a Solução)
A análise das correlações e distribuições no Dashboard revelou:
* **Correlação Crítica:** O **Gasto Histórico (`Gasto_Total_BRL`)** e o **Nível de Progresso (`Nivel_Atual`)** são os preditores mais fortes para a compra.
* **Ineficiência:** A Taxa de Conversão geral é baixa (~10%), mas a conversão é **dramaticamente maior** (4x ou mais) no segmento de jogadores que **já gastaram** (Comprovado pelo Gráfico de Barras Empilhadas).
* **Timing:** O Nível Médio dos jogadores que compraram é superior, indicando que a oferta é mais relevante quando acionada por um **gatilho de progresso** (nível alto).

## 3. Conclusões e Sugestões de Ação Estratégica

### 3.1. Conclusão Final do Projeto
A análise demonstrou que a estratégia de ofertas generalistas é ineficiente e desperdiça potencial de LTV. A solução não está em exibir a oferta para mais pessoas, mas em aprimorar a **segmentação e o timing** com base no comportamento do jogador.

### 3.2. Sugestões de Ação Imediata (Otimização da Oferta X)

Baseado nos insights da modelagem, as seguintes ações são recomendadas:

| Ação Estratégica | Insight de Suporte no Dashboard | Impacto no Negócio |
| :--- | :--- | :--- |
| **Ação 1: Priorizar o *Upsell*** | **Gráfico de Barras Empilhadas:** Foca nos Pagantes, cuja propensão à compra é dramaticamente maior. | Maximização do **LTV** e maior Retorno sobre Investimento (ROI) em marketing. |
| **Ação 2: Otimização do *Timing*** | **Gráfico de Nível Médio:** Implementar o gatilho da Oferta X com base no **Nível de Progresso** (níveis mais altos), onde a relevância é máxima. | Aumento da **Taxa de Conversão** ao transformar a oferta em uma solução valiosa no momento certo. |
| **Ação 3: Converter Alto Potencial** | **Gráfico de Dispersão:** Direcionar Ofertas "Porta de Entrada" (baixo valor) para jogadores com **Alto Tempo Jogado e Gasto Zero** (clientes de Alto LTV Potencial). | Aumentar a base de pagantes e quebrar a barreira da primeira compra. |
