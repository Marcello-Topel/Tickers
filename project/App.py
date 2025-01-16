import dash
from dash import html, dcc
from layout import criar_layout
from callbacks import registrar_callbacks

app = dash.Dash(__name__)

app.layout = criar_layout()

registrar_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
