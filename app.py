import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
from dash import html

# Carregar seu CSV
df = pd.read_csv('dados/df_agrupado.csv')  # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo

# Import App dash: 
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

#install buttom:

buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="me-1"),
        dbc.Button("Secondary", color="secondary", className="me-1"),
        dbc.Button("Success", color="success", className="me-1"),
        dbc.Button("Warning", color="warning", className="me-1"),
        dbc.Button("Danger", color="danger", className="me-1"),
        dbc.Button("Info", color="info", className="me-1"),
        dbc.Button("Light", color="light", className="me-1"),
        dbc.Button("Dark", color="dark", className="me-1"),
        dbc.Button("Link", color="link"),
    ]
)

# Criar gráfico (exemplo com gráfico de dispersão)
fig = px.scatter(df, x='Gestor_Responsavel', y='Valor_final_negociado_formatado', title="Exemplo de Gráfico", color='Valor_final_Inicial_de_Cotacao_formatado')

# Definir o layout do aplicativo Dash
app.layout = html.Div([
    html.H1("Dash Board Suprimentos Liliane Amanda", style={'text-align': 'center'}),
    dcc.Graph(figure=fig)
])

# Rodar o servidor local
if __name__ == '__main__':
    app.run(debug=True)
