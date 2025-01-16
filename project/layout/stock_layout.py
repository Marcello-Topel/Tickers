# layout/stock_layout.py
import dash
from dash import dcc, html
from layout.input_layout import create_input_layout

# Função para criar o layout do gráfico
def create_stock_layout():
    return html.Div(id='app-container', children=[
        html.H1("Dados de Ações em Tempo Real", style={'color': '#00bcd4', 'fontSize': '48px'}),
        create_input_layout(),
        html.Div(
            dcc.Graph(id='stock-graph'),
            className='graph-container'
        ),
        dcc.Interval(id='interval-component', interval=10000, n_intervals=0)
    ])
