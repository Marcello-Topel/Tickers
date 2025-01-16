# layout/input_layout.py
import dash
from dash import dcc, html

# Função para criar o layout da entrada do ticker
def create_input_layout():
    return html.Div([
        html.Label("Digite os tickers das ações separados por vírgula (ex: AAPL,MSFT):", style={'color': '#dddddd', 'fontSize': '20px'}),
        dcc.Input(id='stock-input', value='PBR,BBAS3.SA', type='text', debounce=True, style={'width': '70%', 'fontSize': '24px', 'padding': '10px'}),
    ])
