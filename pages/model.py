import dash
from dash import html , dcc
import pandas as pd
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

layout = dbc.Container(
    [
        dbc.Row(
            [
            dbc.Col(
                html.Div(
                        [
                            html.H4("MDS-01",style={'marginTop':'4rem','textAlign':'center'}),
                            html.H4("MDS-02",style={'textAlign':'center'})
                            
                        ]
                    )                                                                                  
                )
            ]
        )
    ]
)