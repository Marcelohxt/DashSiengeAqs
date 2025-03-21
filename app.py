import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Carregar seu CSV
df = pd.read_csv('dados/df_agrupado.csv')  # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo

# Inicializar o app Dash
app = dash.Dash(__name__)

# Criar gráfico (exemplo com gráfico de dispersão)
fig = px.scatter(df, x='Coluna_X', y='Coluna_Y', title="Exemplo de Gráfico", color='Coluna_Cor')

# Definir o layout do aplicativo Dash
app.layout = html.Div([
    html.H1("Meu Dashboard", style={'text-align': 'center'}),
    dcc.Graph(figure=fig)
])

# Rodar o servidor local
if __name__ == '__main__':
    app.run_server(debug=True)
