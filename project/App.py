# app.py
import dash
from callbacks.stock_callbacks import register_callbacks
from layout.stock_layout import create_stock_layout

app = dash.Dash(__name__)
app.title = 'Dados de Ações em Tempo Real'

# Definir o layout da aplicação
app.layout = create_stock_layout()

# Registrar os callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
