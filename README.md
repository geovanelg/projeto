# Previsão de Vendas de Combustível

Este é um projeto de previsão de vendas de combustível usando aprendizado de máquina.

## Objetivo

O objetivo deste projeto é prever as vendas de combustível com base em dados históricos de vendas.

## Funcionalidades

- Consulta dados históricos de vendas de combustível de um banco de dados Oracle.
- Pré-processa os dados para prepará-los para a modelagem.
- Treina um modelo de regressão florestal aleatória usando os dados de treinamento.
- Avalia o desempenho do modelo usando métricas como Mean Squared Error (MSE), Mean Absolute Error (MAE) e R^2 Score.
- Gera visualizações dos resultados do modelo.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python: cx_Oracle, pandas, numpy, scikit-learn, matplotlib, seaborn

## Conjunto de Dados

Os dados utilizados neste projeto foram coletados do banco de dados Oracle e consistem em registros de vendas de combustível para os anos de 2022 e 2023.

## Pré-processamento dos Dados

Os dados foram pré-processados para transformar as datas em dias desde o início do intervalo e realizar outras etapas de limpeza e formatação necessárias.

## Modelagem e Treinamento

Um modelo de regressão foi treinado usando Random Forest Regressor com 100 estimadores. Os dados foram divididos em conjunto de treino e teste, e o modelo foi avaliado usando métricas como MSE, MAE e R².

## Avaliação do Modelo

O modelo alcançou os seguintes resultados na avaliação:
- MSE: 0.33
- MAE: 0.44
- R²: 0.86

## Resultados

Os resultados da previsão foram plotados em um gráfico para visualização.

## Próximos Passos

- Explorar técnicas avançadas de modelagem para melhorar o desempenho do modelo.
- Incorporar dados adicionais para enriquecer a análise.
- Realizar análises de tendências e sazonalidade nos dados.

## Contribuindo

Se você quiser contribuir para este projeto, siga estas etapas:

- Faça um fork do projeto
- Crie sua própria branch (git checkout -b feature/sua-feature)
- Faça commit das suas alterações (git commit -am 'Adicione uma nova feature')
- Faça push para a branch (git push origin feature/sua-feature)
- Crie um novo Pull Request


