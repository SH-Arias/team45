import pandas as pd
from dash import html , dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from app import list_of_images

register_page(__name__, path="/dsm")
data = {'Code': [300, 200, 601], 
    'X': [5078011.1380, 5078011.5880, 5078078.5400],
    'Y': [2342928.8960, 2342930.8270, 2342905.5430],
    'Z': [1343.8460, 1341.7580, 1292.7640]
}

df = pd.DataFrame.from_dict(data)
table = dbc.Table.from_dataframe(
    df, striped=True, bordered=True, hover=True, index=False
)


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
                            html.H3('DIGITAL SURFACE MODELS'),
                            html.Br(),
                            html.P('Heres how raw data looks like:'),
                            table,
                            html.P('There are 11 data-sets representing equal number of sections \
                                of the Toledo-Zamore transmmision line. \
                                This data-sets are shown are displayed as \
                                rendered using the Open3D Python library.\
                                '),
                            html.P('The colors vary from blue to red on the images according to the X coordinate, being blue the lowest and red the higher position along that axis.')
                            ]
                        ),
                        width={'size':4}
                    )
                ]
            )
        ]
    )
)