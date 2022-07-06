import pandas as pd
from dash import html , dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

list_of_images = [
    'section1','section2','section3','section4',
    'section5','section6','section7','section8',
    'section9','section10','section11'
    ]

register_page(__name__, path="/dsm")

layout = dbc.Container(
    html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                                    [
                                        dcc.Dropdown(
                                        id='image-dropdown',
                                        options=[{'label': i, 'value': i} for i in list_of_images],
                                        value=list_of_images[0]
                                        ),
                                        html.Div(html.Img(id='image',width='100%')),     
                                    ]
                            ),
                            width={'size':8}
                        ),
                    dbc.Col(html.Div(
                            [
                            html.P('Data sets rendered by using the Open3D Python library')
                            ]
                        ),
                        width={'size':4}
                    )
                ]
            )
        ]
    )
)