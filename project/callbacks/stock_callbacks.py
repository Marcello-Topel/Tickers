# callbacks/stock_callbacks.py
import dash
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from utils.stock_data import get_stock_data

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
            previous_close = data['Close'].iloc[-2]
            price_change = latest_close - previous_close
            price_change_percent = (price_change / previous_close) * 100

            # Definir a cor da barra com base no movimento de preço
            if price_change == 0:
                color = 'gray'  # Preço não mudou
            elif price_change > 0:
                color = 'green'  # Preço subiu
            else:
                color = 'red'  # Preço caiu

            price_change_text = f'{price_change_percent:+.2f}%'

            fig.add_trace(go.Bar(
                x=[ticker],
                y=[latest_close],
                name=f'{ticker}',
                marker=dict(color=color),
                width=0.5,
                orientation='v',
                text=f'{latest_close:.2f} USD ({price_change_text})',
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
