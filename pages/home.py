#import dash
from dash import html , dcc
import pandas as pd
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/")

#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container(
    [
        dbc.Row(
            [
                html.H2('DS4A / Colombia - Cohort 6',style={'marginTop':'4rem','textAlign':'center','color':'#003B92','marginBottom':'5rem'}),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    #html.Div(html.Img(src=app.get_asset_url('imageedit_1_6955781055.png'), style={'width':'70%', 'textAlign':'center'})),
                    html.Div(html.Img(src=('https://storage.googleapis.com/lidar-data-01/images/isaLogo.png'), style={'width':'50%', 'display':'inline-block', 'margin-top':'7%', 'margin-left':'55%'})),
                    ),
                dbc.Col(
                    #html.Div(html.Img(src=app.get_asset_url('imageedit_1_6955781055.png'), style={'width':'70%', 'textAlign':'center'})),
                    html.Div(html.Img(src=('https://storage.googleapis.com/lidar-data-01/images/team45logo.png'), style={'width':'50%', 'display':'inline-block'})),
                    )
            ]
        ),
        dbc.Row(
            [
                html.H2('CHARACTERIZATION AND CLASSIFICATION OF LIDAR SENSOR DATA',style={'marginTop':'4rem','textAlign':'center','color':'#50006e','marginBottom':'5rem'}),
            ]
        ),
    ]
)