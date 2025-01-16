import yfinance as yf
import plotly.graph_objs as go
from dash import Input, Output
import pandas as pd

def obter_dados_acao(ticker):
    try:
        acao = yf.Ticker(ticker)
        dados = acao.history(period='1d', interval='1m')  # Dados de 1 dia com intervalo de 1 minuto
        if dados.empty:
            raise ValueError(f"Nenhum dado encontrado para o ticker: {ticker}.")
        return dados
    except Exception as e:
        print(f"Erro ao obter dados para {ticker}: {e}")
        return pd.DataFrame()

def registrar_callbacks(app):
    @app.callback(
        Output('stock-graph', 'figure'),
        [Input('stock-input', 'value'), Input('interval-component', 'n_intervals')]
    )
    def atualizar_grafico(tickers, n):
        tickers_lista = [ticker.strip().upper() for ticker in tickers.split(',') if ticker.strip()]
        if not tickers_lista:
            return go.Figure()

        fig = go.Figure()
        for ticker in tickers_lista:
            dados = obter_dados_acao(ticker)
            if dados.empty:
                continue

            fechamento_mais_recente = dados['Close'].iloc[-1]

            if n == 0:
                cor = 'gray'  # Cor inicial
            else:
                fechamento_anterior = dados['Close'].iloc[-2]
                cor = 'green' if fechamento_mais_recente > fechamento_anterior else 'red' if fechamento_mais_recente < fechamento_anterior else 'gray'

            fig.add_trace(go.Bar(
                x=[ticker],
                y=[fechamento_mais_recente],
                name=f'{ticker}',
                marker=dict(color=cor),
                width=0.5,  # Largura da barra
                orientation='v',  # Orientação vertical
                text=f'{fechamento_mais_recente:.2f} USD',  # Texto exibido na barra
                textposition='inside',  # Posição do texto
                texttemplate='%{text}',  # Formatação do texto
                hoverinfo='x+y+text',  # Informações ao passar o mouse
                hoverlabel=dict(bgcolor='white', font_size=13, font_family="Lato, sans-serif")  # Estilo do hover
            ))

        fig.update_layout(
            title=f'Preços Atuais das Ações: {", ".join(tickers_lista)}',
            title_font=dict(size=20, color='#2E3D49', family="Lato, sans-serif"),
            xaxis_title='Ação',
            yaxis_title='Preço (USD)',
            xaxis_tickangle=-45,  # Ângulo dos ticks no eixo X
            plot_bgcolor='#F4F4F4',  # Cor de fundo do gráfico
            paper_bgcolor='#FFFFFF',  # Cor de fundo da área do gráfico
            margin=dict(t=50, b=50, l=50, r=50),  # Margens
            showlegend=False,  # Ocultar legenda
            hovermode="closest",  # Modo de hover
            font=dict(color='#2E3D49', family="Lato, sans-serif")  # Fonte do gráfico
        )

        return fig
