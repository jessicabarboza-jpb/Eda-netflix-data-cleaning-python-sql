# 1. Importação de Bibliotecas
import pandas as pd
import sqlite3
import plotly.express as px

# 2. Ingestão de Dados
# O caminho está configurado de forma relativa para facilitar a execução local ou no GitHub
df = pd.read_csv('netflix_titles.csv')

# 3. Criação do Banco de Dados Relacional Temporário
conn = sqlite3.connect(':memory:')
df.to_sql('netflix', conn, index=False)

# ---------------------------------------------------------
# ANÁLISE 1: Proporção Filmes vs Séries (SQL)
# ---------------------------------------------------------
query_tipos = """
    SELECT type, COUNT(*) as quantidade 
    FROM netflix 
    GROUP BY type
"""
resultado_tipos = pd.read_sql(query_tipos, conn)

grafico_pizza = px.pie(
    resultado_tipos, 
    values='quantidade', 
    names='type', 
    title='Proporção do Catálogo: Filmes vs Séries',
    color_discrete_sequence=['#E50914', '#564d4d']
)
grafico_pizza.show()

# ---------------------------------------------------------
# ANÁLISE 2: Evolução de Lançamentos Temporais (SQL)
# ---------------------------------------------------------
query_anos = """
    SELECT release_year, COUNT(*) as quantidade 
    FROM netflix 
    GROUP BY release_year 
    ORDER BY release_year
"""
resultado_anos = pd.read_sql(query_anos, conn)

grafico_linha = px.line(
    resultado_anos, 
    x='release_year', 
    y='quantidade', 
    title='Evolução de Lançamentos Globais por Ano',
    markers=True,
    color_discrete_sequence=['#E50914']
)
grafico_linha.show()

# ---------------------------------------------------------
# ANÁLISE 3: Top 10 Categorias - Limpeza e Visualização (Pandas)
# ---------------------------------------------------------
# Separação das strings em listas
df['generos_separados'] = df['listed_in'].str.split(', ')

# Normalização do dataset (uma linha por gênero)
df_explodido = df.explode('generos_separados')

# Recálculo das métricas com dados limpos
top_10_real = df_explodido['generos_separados'].value_counts().head(10).reset_index()
top_10_real.columns = ['categoria', 'quantidade']

# Geração do Gráfico de Barras
grafico_barras = px.bar(
    top_10_real, 
    x='quantidade', 
    y='categoria', 
    title='Top 10 Gêneros Individuais (Base Normalizada)',
    orientation='h', 
    color='quantidade', 
    color_continuous_scale='Blues' 
)

grafico_barras.update_layout(yaxis={'categoryorder':'total ascending'})
grafico_barras.show()
