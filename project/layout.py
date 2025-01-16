from dash import html, dcc

def criar_layout():
    return html.Div([
        html.H1("Dados de Ações em Tempo Real", style={'textAlign': 'center', 'color': '#2E3D49'}),
        html.Label("Digite os tickers das ações separados por vírgula (ex: AAPL,MSFT):", style={'color': '#2E3D49'}),
        dcc.Input(id='stock-input', value='', type='text', debounce=True, style={'width': '50%'}),
        dcc.Graph(id='stock-graph'),
        dcc.Interval(id='interval-component', interval=10000, n_intervals=0)  # Atualiza a cada 10 segundos
    ])
