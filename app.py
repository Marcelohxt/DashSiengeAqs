import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc

# Carregar seu CSV
df = pd.read_csv('dados/df_agrupado.csv')  # Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo




app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

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
