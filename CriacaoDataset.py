import numpy as np
import pandas as pd

N_JOGADORES = 5000
np.random.seed(42) # Garante que os resultados sejam reproduzíveis

# 1. Geração das Variáveis Comportamentais

# Nível Atual (Distribuição tendendo a mais jogadores nos níveis iniciais)
nivel = np.random.randint(1, 101, N_JOGADORES)

# Dias Desde a Instalação (Distribuição exponencial para simular abandono precoce)
dias_vida = np.random.exponential(scale=30, size=N_JOGADORES).astype(int) + 1

# Tempo Jogado (Correlacionado com o tempo de vida e nível)
tempo_jogado_horas = (nivel * 0.5) + (dias_vida * 0.8) + np.random.normal(0, 5, N_JOGADORES)
tempo_jogado_horas = np.maximum(1, tempo_jogado_horas).astype(int)

# Itens Raros Possuídos (Começa baixo)
itens_raros = np.random.poisson(lam=(nivel / 20), size=N_JOGADORES)
itens_raros = np.maximum(0, itens_raros)

# 2. Geração da Variável de Gasto (Simulando a Regra dos 80/20)

# 85% dos jogadores são 'Não Pagantes' (Gasto Total = 0 ou muito próximo)
gasto_total = np.zeros(N_JOGADORES)
pagantes_indices = np.random.choice(N_JOGADORES, size=int(N_JOGADORES * 0.15), replace=False)

# 15% são 'Pagantes'
# Aplicamos uma distribuição pesada para simular 'Baleias' (Lognormal)
gasto_pagantes = np.random.lognormal(mean=2.5, sigma=1.0, size=len(pagantes_indices)) * 10
gasto_total[pagantes_indices] = gasto_pagantes.round(2)

# 3. Geração da Variável Alvo: COMPROU_OFERTA_X (Otimização de Ofertas)

# A probabilidade de compra AUMENTA com o nível e o gasto histórico
prob_compra = (0.02 +
               (nivel / 100) * 0.05 +
               np.log1p(gasto_total) * 0.05 +
               (tempo_jogado_horas / 200) * 0.05
              )
prob_compra = np.clip(prob_compra, 0, 0.5) # Limita a probabilidade máxima

# Simula a compra (0 ou 1)
comprou_oferta_X = np.random.binomial(n=1, p=prob_compra)


# 4. Criação do DataFrame
df = pd.DataFrame({
    'ID_Jogador': np.arange(1, N_JOGADORES + 1),
    'Dias_Desde_Instalacao': dias_vida,
    'Nivel_Atual': nivel,
    'Tempo_Jogado_Horas': tempo_jogado_horas,
    'Itens_Raros_Possuidos': itens_raros,
    'Gasto_Total_BRL': gasto_total,
    'COMPROU_OFERTA_X': comprou_oferta_X
})