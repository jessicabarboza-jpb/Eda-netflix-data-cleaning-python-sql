# Análise Exploratória e Tratamento de Dados: Catálogo Netflix

## Descrição do Projeto
Projeto de análise de dados focado em extrair inteligência de negócios a partir do catálogo global da Netflix. O objetivo principal foi demonstrar a importância da validação estrutural dos dados antes da etapa de visualização, garantindo que as métricas reflitam a realidade do cenário analisado.

## Stack Tecnológica
* **Linguagem:** Python e SQL
* **Bibliotecas:** Pandas (Manipulação de dados), SQLite3 (Consultas relacionais) e Plotly Express (Visualização interativa)
* **Ambiente:** Google Colab / Jupyter Notebook

## O Problema de Negócio e o Desafio dos Dados
A proposta inicial era identificar a proporção de formatos (Filmes vs. Séries), a evolução de lançamentos temporais e o Top 10 das categorias com maior volume de títulos. 

Durante a Análise Exploratória de Dados (EDA), identificou-se uma inconsistência na estrutura do dataset original (Kaggle). A coluna `listed_in` agrupava múltiplos gêneros em uma única string separada por vírgulas para cada título. A contagem direta (via `GROUP BY` em SQL ou `value_counts` em Pandas) gerava categorias compostas e distorcia o volume real de cada nicho, impossibilitando uma análise de Pareto precisa.

## Solução Técnica Aplicada
Para garantir a integridade da métrica de categorias, o pipeline de dados foi ajustado utilizando métodos avançados de manipulação de strings e arrays em Pandas:

1. **Separação de Elementos:** Aplicação de `str.split(', ')` para converter a string de categorias em uma lista iterável dentro de cada célula.
2. **Explosão de Dados:** Utilização da função `explode()` para transformar cada item da lista em uma nova linha independente (row), mantendo o índice original associado ao título.
3. **Recálculo:** Agrupamento e contagem exata (`value_counts`) sob a nova estrutura normalizada.

## Insight Analítico
A correção da métrica revelou que a categoria líder isolada do catálogo é **"International Movies"**, seguida por "Dramas" e "Comedies".

Este achado transcende o dado limpo e evidencia a macroestratégia da companhia. Diante da saturação e da alta concorrência no mercado norte-americano, a liderança em conteúdo internacional comprova a estratégia global da plataforma em adquirir e produzir conteúdos focados em mercados estrangeiros para tracionar sua base de assinantes em escala mundial.

## Como Executar
O arquivo principal contendo todos os scripts de manipulação e geração de gráficos é o `analise_netflix.ipynb`. Para reproduzir, certifique-se de que o arquivo `netflix_titles.csv` esteja no mesmo diretório de execução.
