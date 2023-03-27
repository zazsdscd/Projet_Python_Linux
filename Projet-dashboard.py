# -*- coding: utf-8 -*-

import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Chargement des données
df = pd.read_csv('/home/ubuntu/prices.csv', sep=',', names=['Date', 'prix'], na_values=[''])
df['prix'] = df['prix'].astype(float)
df['Date'] = pd.to_datetime(df['Date'])
ts = pd.Series(df['prix'].values, index=df['Date'])

# Calcul des statistiques
volatility = round(ts.pct_change().std() * 100, 2)
mean_price = '${:,.2f}'.format(round(ts.mean(), 2))
current_price = '${:,.2f}'.format(round(ts.iloc[-1], 2))
daily_return = round((ts.iloc[-1] - ts.iloc[0]) / ts.iloc[0] * 100, 2)

# Initialisation de l'application Dash
app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.Div(children=[html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-ajAJF0MnK35cgI51EuyAjWHiRYTTjKZgew&usqp=CAU',
                 style={'width': '20%'}),
        html.H3(children='XRP Presentation',
                style={'text-align': 'center', 'font-weight': 'bold', 'font-size': '45px', 'margin-left': '40px',
                       'margin-right': '40px'}),
        html.Table(
            children=[
                html.Tr(
                    children=[
                        html.Td(children=' '),
                        html.Td(children='Performance'),
                    ]
                ),
                html.Tr(
                    children=[
                        html.Td(children='Daily return'),
                        html.Td(children='{:.2f}%'.format(daily_return),
                                style={'color': 'red' if daily_return < 0 else 'green'})
                    ]
                ),
                html.Tr(
                    children=[
                        html.Td(children='Volatility'),
                        html.Td(children=f'{volatility}%',style={'color': 'red' if volatility > 10 else 'green'})]
                ),
                html.Tr(
                    children=[
                        html.Td(children='Mean'),
                        html.Td(children=mean_price)
                    ]
                ),
                html.Tr(
                    children=[
                        html.Td(children='Actual Price'),
                        html.Td(children=current_price)
                    ]
                )
            ]
        ),
    ], style={'display': 'flex'}),

    dcc.Graph(
        id='xrp-price-chart',
        figure={
            'data': [{
                'x': df['Date'],
                'y': df['prix'],
                'type': 'line'
            }], 'layout': {
                'title': 'XRP Price over time',
                'xaxis': {'title': 'Date'},
                'yaxis': {'title': 'Price'}
            }
        }
    )
])

if __name__ == '__main__':
        app.run_server(debug=True,port=8050, host='0.0.0.0')
                                                               
