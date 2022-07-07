import dash
from dash import html , dcc
import pandas as pd
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/model")

lista = ["K-Nearest Neighbour","Decision Tree Classifier","Random random forest","Extra Tree Classifier"]

layout = dbc.Container(
    [
        dbc.Row(
            [
        
            html.Div(
                    [
                        html.H4("Models for classification",style={'marginTop':'4rem','textAlign':'center'}),
                        html.Br(),
                        html.P("In order to accoplish the objective of creating a model to clasify lidar data based on\
                            data already classified, the following models were tested:"),
                        html.Ol([html.Li(x) for x in lista]),
                        html.P("We obtained the best results using the extra tree classifier\
                            but in no case more than 50 percent accuaracy, this means the model assigned \
                            most of the time code 300 for less than 1 meter high tree, and natural terrain. This made \
                                necessary the implementation of a data aumentation algorithm "),
                        html.Br(),
                        html.P()
                        
                    ]
                )                                                                                  
                
            ]
        )
    ]
)