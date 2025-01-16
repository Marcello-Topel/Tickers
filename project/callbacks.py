# callbacks.py
import dash
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d', interval='1m')
        if data.empty:
            raise ValueError(f"Nenhum dado encontrado para o ticker: {ticker}.")
        return data
    except Exception as e:
        print(f"Erro ao obter dados para {ticker}: {e}")
        return pd.DataFrame()

def register_callbacks(app):
    @app.callback(
        Output('stock-graph', 'figure'),
        [Input('stock-input', 'value'), Input('interval-component', 'n_intervals')]
    )
    def update_graph(tickers, n):
        tickers_list = [ticker.strip().upper() for ticker in tickers.split(',') if ticker.strip()]
        if not tickers_list:
            return go.Figure()

        fig = go.Figure()
        for ticker in tickers_list:
            data = get_stock_data(ticker)
            if data.empty:
                continue

            latest_close = data['Close'].iloc[-1]
            color = 'gray' if n == 0 else ('green' if latest_close > data['Close'].iloc[-2] else 'red')
            fig.add_trace(go.Bar(
                x=[ticker],
                y=[latest_close],
                name=f'{ticker}',
                marker=dict(color=color),
                width=0.5,
                orientation='v',
                text=f'{latest_close:.2f} USD',
                textposition='inside',
                texttemplate='%{text}',
                hoverinfo='x+y+text',
                hoverlabel=dict(bgcolor='white', font_size=13, font_family="Lato, sans-serif")
            ))

        fig.update_layout(
            title=f'Preços Atuais das Ações: {", ".join(tickers_list)}',
            title_font=dict(size=20, color='#FFFFFF', family="Lato, sans-serif"),
            xaxis_title='Ação',
            yaxis_title='Preço (USD)',
            xaxis_tickangle=-45,
            plot_bgcolor='black',
            paper_bgcolor='black',
            margin=dict(t=50, b=50, l=50, r=50),
            showlegend=False,
            hovermode="closest",
            font=dict(color='#FFFFFF', family="Lato, sans-serif")
        )

        return fig
