import dash
from dash import dcc
from dash import html
from dash import dcc, html
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
from dash import html

# Carregar seu CSV
df = pd.read_csv('dados/df_agrupado.csv')  # Substitua pelo caminho correto do seu arquivo

# Inicializar o app com tema escuro
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Criar gráficos
fig1 = px.scatter(df, x='Gestor_Responsavel', y='Valor_final_negociado_formatado', title="Valores Negociados", color='Valor_final_Inicial_de_Cotacao_formatado')
fig2 = px.bar(df, x='Gestor_Responsavel', y='Valor_final_negociado_formatado', title="Comparação de Valores", color='Valor_final_Inicial_de_Cotacao_formatado')
fig3 = px.pie(df, names='Gestor_Responsavel', values='Valor_final_negociado_formatado', title="Distribuição de Valores")
fig4 = px.line(df, x='Gestor_Responsavel', y='Valor_final_negociado_formatado', title="Evolução dos Valores", markers=True)

# Botões estilizados
buttons = html.Div(
    [
        dbc.Button("Atualizar", color="primary", className="me-2"),
        dbc.Button("Exportar Dados", color="success", className="me-2"),
        dbc.Button("Configurações", color="info", className="me-2"),
    ],
    className="d-flex justify-content-center my-3"
)

# Barra de pesquisa
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="text", placeholder="Pesquisar..."), width=8),
        dbc.Col(dbc.Button("Buscar", color="primary"), width=2)
    ],
    className="mb-4 d-flex justify-content-center"
)

# Layout do aplicativo
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1("Dashboard Suprimentos Liliane Amanda", className="text-center my-4")
            )
        ),
        search_bar,
        buttons,
        dbc.Row(
            [
                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig1)])), width=6),
                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig2)])), width=6)
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig3)])), width=6),
                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig4)])), width=6)
            ]
        ),

        dbc.Row(
            [
                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig3)])), width=6),
                dbc.Col(dbc.Card(dbc.CardBody([dcc.Graph(figure=fig4)])), width=6)
            ]
        ),
        
    ],
    fluid=True
)

# Rodar o servidor local
if __name__ == '__main__':
    app.run(debug=True)

