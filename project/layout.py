import dash
from dash import dcc, html

def create_layout():
    return html.Div(id='app-container', children=[
        html.H1("Dados de Ações em Tempo Real", style={'color': '#00bcd4', 'fontSize': '48px'}),
        html.Label("Digite os tickers das ações separados por vírgula (ex: AAPL,MSFT):", style={'color': '#dddddd', 'fontSize': '20px'}),
        dcc.Input(id='stock-input', value='PBR,BBAS3.SA', type='text', debounce=True, style={
            'width': '70%',
            'fontSize': '24px',
            'padding': '12px',
            'marginBottom': '30px',
            'borderRadius': '8px',
            'border': '2px solid #00bcd4',
            'backgroundColor': '#333',
            'color': '#fff',
            'outline': 'none'
        }),
        html.Div(dcc.Graph(id='stock-graph'), className='graph-container'),
        dcc.Interval(id='interval-component', interval=10000, n_intervals=0)
    ])
