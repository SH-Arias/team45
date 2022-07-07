import dash
from dash import html , dcc
import pandas as pd
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

register_page(__name__, path="/model")

lista = ["K-Nearest Neighbour","Decision Tree Classifier","Random random forest","Extra Tree Classifier"]
lista2 = ["Random Sample","Cluster Sample","Displacement"]
data = {'Code': [300, 200, 601], 
    'X': [5078011.1380, 5078011.5880, 5078078.5400],
    'Y': [2342928.8960, 2342930.8270, 2342905.5430],
    'Z': [1343.8460, 1341.7580, 1292.7640]
}


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
                        html.P("We tested various techniques for that process including:"),
                        html.Ol([html.Li(x) for x in lista2]),
                        html.Br(),
                        html.H4("Results using extra tree classifier"),
                        html.Div(html.Img(src=('https://storage.googleapis.com/lidar-data-01/images/classification.png'), style={'width':'70%', 'textAlign':'center'}))
                    ]
                )                                                                                  
                
            ]
        )
    ]
)