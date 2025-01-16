import dash
import layout
import callbacks

app = dash.Dash(__name__)
app.title = 'Dados de Ações em Tempo Real'

# Layout da aplicação
app.layout = layout.create_layout()

# Registrando os callbacks
callbacks.register_callbacks(app)

# Iniciando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
