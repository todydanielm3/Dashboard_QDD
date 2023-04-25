from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from colorspacious import cspace_converter
import matplotlib as mpl
import plotly.io as pio



# Create a Dash app
app = Dash(__name__)
app.title = 'Contrato Nº 001-2018'


# Load the data
df = pd.read_csv('dados1.csv',sep=';',header=0)
d2 = pd.read_csv('dados2.csv',sep=';',header=0)
d3 = pd.read_csv('dados3.csv',sep=';',header=0)

print(d2.head())
print(d2.columns)

print(d3.head())
print(d3.columns)

#tratando dados 

num_previsão = [float(v.replace('R$','').replace('.','').replace(',','.')) for v in df['PREVISÃO']]
num_bloqueio = [float(v.replace('R$','').replace('.','').replace(',','.')) for v in df['BLOQUEIO']]
num_remanejamento = [float(v.replace('R$','').replace('.','').replace(',','').replace('-','')) for v in df['REMANEJAMENTO']]



num_despesa_autorizada = [float(v.replace('R$','').replace('.','').replace(',','.')) for v in d2['DESPESA AUTORIZADA']]
num_despesa_executada = [float(v.replace('R$','').replace('.','').replace(',','.')) for v in d2['DESPESA EXECUTADA']]

num_despesa_autorizada3 = [float(v.replace('R$','').replace('.','').replace(',','.')) for v in d3['DESPESA AUTORIZADA']]
num_despesa_executada3 = [float(v.replace('R$','').replace('.','').replace(',','.')) for v in d3['DESPESA EXECUTADA']]


#graficos Quadro Demonstrativo de Despesas (QDD) - 2022

fig1 = px.bar(d2, x='Pessoal', y=num_despesa_autorizada, color='Grupo de Despesa', title='DESPESAS AUTORIZADAS')
layout = go.Layout(
    title='DESPESAS AUTORIZADAS',
    xaxis=dict(
        title='Pessoal',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='DESPESA AUTORIZADA',
        titlefont_size=16,
        tickfont_size=14,
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig1.update_layout(layout)


fig2 = px.bar(d2, x='Pessoal', y=num_despesa_executada, color='Grupo de Despesa', title='DESPESAS EXECUTADAS')
layout = go.Layout(
    title='DESPESAS EXECUTADAS',
    xaxis=dict(
        title='Pessoal',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='DESPESA EXECUTADA',
        titlefont_size=16,
        tickfont_size=14,
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig2.update_layout(layout)





#fig5, ax = plt.subplots()
#ax.pie(num_previsão, labels=df['Pessoal'], autopct='%1.1f%%')

fig6 = go.Figure(data=[go.Pie(labels=d2['Pessoal'], values=num_despesa_autorizada, title='DESPESAS AUTORIZADAS')])
fig7 = go.Figure(data=[go.Pie(labels=d2['Pessoal'], values=num_despesa_executada, title='DESPESAS EXECUTADAS')])


#fig8 = px.bar_polar(df, r='DESPESA AUTORIZADA', theta='Pessoal', color='Grupo de Despesa', title='DESPESAS AUTORIZADAS', template='plotly_white')
fig8 = px.bar_polar(df,r='BLOQUEIO', theta='Pessoal', color='RUBRICA', title='BLOQUEIO DE DESPESA', template='plotly_white')

fig9 = px.bar_polar(df, r='PREVISÃO', theta='Pessoal', color='RUBRICA', title='DESPESAS PREVISTAS', template='plotly_white')

# Graficos d agragação com as UPAS

figura1 = px.bar(d3, x='Pessoal', y=num_despesa_autorizada3, color='Grupo de Despesa', title='DESPESAS AUTORIZADAS')
layout = go.Layout(
    title='DESPESAS AUTORIZADAS',
    xaxis=dict(
        title='Pessoal',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='DESPESA AUTORIZADA',
        titlefont_size=16,
        tickfont_size=14,
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
figura1.update_layout(layout)

figura2 = px.bar(d3, x='Pessoal', y=num_despesa_executada3, color='Grupo de Despesa', title='DESPESAS EXECUTADAS')
layout = go.Layout(
    title='DESPESAS EXECUTADAS',
    xaxis=dict(
        title='Pessoal',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='DESPESA EXECUTADA',
        titlefont_size=16,
        tickfont_size=14,
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
figura2.update_layout(layout)

figura3 = go.Figure(data=[go.Pie(labels=d3['Pessoal'], values=num_despesa_autorizada3, title='DESPESAS AUTORIZADAS')])
figura4 = go.Figure(data=[go.Pie(labels=d3['Pessoal'], values=num_despesa_executada3, title='DESPESAS EXECUTADAS')])




# Create the app layout
app.layout = html.Div([
    html.H1('QUADRO DEMONSTRATIVO DE DESPESAS (QDD)'),
    html.H3('FONTE DE RECURSO: CONTRATO Nº 001/2018'),
    
    html.Div([
    #mostrando grafico e configurando o tamanho
    dbc.Col(dcc.Graph(figure=fig1), width=6),
    dbc.Col(dcc.Graph(figure=fig6), width=6),

    ],style={'display': 'flex'}),



    html.Div([
    dbc.Col(dcc.Graph(figure=fig2), width=6),
    dbc.Col(dcc.Graph(figure=fig7), width=6),
    ],style={'display': 'flex'}),
    

    html.Div([
        html.H1('AGRUPAMENTO COM AS UPAS JÚNIOR', style={'color': 'green'}),
        html.H3('FONTE: Contratos UPAS Júnior'),
    ]),

    html.Div([
        dbc.Col(dcc.Graph(figure=figura1), width=6),
        dbc.Col(dcc.Graph(figure=figura3), width=6),
    ],style={'display': 'flex'}),


    html.Div([
        dbc.Col(dcc.Graph(figure=figura2), width=6),
        dbc.Col(dcc.Graph(figure=figura4), width=6),
    ],style={'display': 'flex'}),




    







    html.Div([
    dbc.Col(dcc.Graph(figure=fig8), width=6),
    dbc.Col(dcc.Graph(figure=fig9), width=6),
    ],style={'display': 'flex'}),


    


    
    

    html.Div([
    html.Div(children='QUADRO DEMONSTRATIVO DE DESPESAS (QDD) – FONTE DE RECURSO: CONTRATO Nº 001/2018', style={'color': 'blue'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=12),
    ]),


    html.Div([
    html.Div(children='AGRUPAMENTO COM AS UPAS JÚNIOR', style={'color': 'green'}),
    html.Div(children='FONTE: Contratos UPAS Júnior', style={'color': 'green'}),
    dash_table.DataTable(data=d3.to_dict('records'), page_size=12),
    ])



])


            

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True,port=8052)


