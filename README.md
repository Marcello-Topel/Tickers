# Tickers - Visualização de Dados de Ações em Tempo Real

O **Ticker** é um aplicativo web interativo desenvolvido em Python que permite monitorar e visualizar as variações de preços de ações em tempo real. Utilizando o framework **Dash** e a API **yfinance**, o aplicativo consulta dados financeiros e apresenta gráficos de barras atualizados automaticamente. A interface é intuitiva e permite monitorar múltiplos tickers simultaneamente, exibindo as variações com cores distintas:

- **Cinza**: Quando o preço não teve alteração significativa.
- **Verde**: Quando o preço aumentou.
- **Vermelho**: Quando o preço diminuiu.

## Tecnologias Utilizadas

Este projeto é desenvolvido com as seguintes tecnologias:

- **Python**: Linguagem de programação principal.
- **Dash**: Framework para criação de aplicativos web interativos.
- **Plotly**: Biblioteca de gráficos interativos, usada para criar o gráfico de barras.
- **yfinance**: API que fornece dados financeiros, como preços de ações em tempo real.
- **CSS**: Para estilizar a interface do usuário.

## Funcionalidades

- **Entrada de Tickers**: O usuário pode digitar um ou mais tickers de ações separados por vírgula (por exemplo: `AAPL, MSFT, TSLA`).
- **Gráfico de Barras Dinâmico**: O gráfico mostra o preço mais recente de cada ação, com cores indicando se o preço subiu (verde), desceu (vermelho) ou permaneceu constante (cinza).
- **Atualização em Tempo Real**: A cada 10 segundos, os preços das ações são atualizados automaticamente, sem a necessidade de recarregar a página.
- **Responsive Design**: O layout se adapta a diferentes tamanhos de tela, permitindo o uso tanto em desktop quanto em dispositivos móveis.
![terceiro](https://github.com/user-attachments/assets/dab2983f-adf1-443e-a798-2a1c7d0467bc)
![quarto](https://github.com/user-attachments/assets/dcb41e63-9fe5-43d6-81ee-473458ef1bbb)


## Como Usar

### 1. Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/Marcello-Topel/Tickers.git
cd Tickers
pip install -r requirements.txt
python app.py
