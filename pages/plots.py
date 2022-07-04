import pandas as pd
import dask.dataframe as dd
from dash import html , dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


register_page(__name__, path="/plots")





features = pd.read_excel('gs://lidar-data-01/datasets/featureCodes.xlsx')
#features = pd.read_excel('gs://lidar-data-01/lidarDataClassified/total_lidar_data.csv')
features = features.sort_values(['Feature Code'], ascending=True).reset_index(drop=True)
features.columns = ["Code", "Description"]
features.reset_index().rename(columns={'index': ''})
table = dbc.Table.from_dataframe(
    features, striped=True, bordered=True, hover=True, index=False
)


#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df_dd = dd.read_csv('gs://lidar-data-01/datasets/MDS-01.csv')
#df_dd = dd.read_csv('gs://lidar-data-01/lidarDataClassified/total_lidar_data.csv')
df = df_dd.compute()
code_data = pd.DataFrame(df["Code"].value_counts()).reset_index()
code_data.columns = ["Code", "Count"]
merged = pd.merge(code_data, features, on="Code")

df_dd2 = dd.read_csv('gs://lidar-data-01/datasets/MDS-02.csv')
df2 = df_dd2.compute()
code_data2 = pd.DataFrame(df2["Code"].value_counts()).reset_index()
code_data2.columns = ["Code", "Count"]
merged2 = pd.merge(code_data2, features, on="Code")
#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

layout = dbc.Container(
    [
        dbc.Row(
            [
                

                dbc.Col(
                    html.Div(
                            [
                                html.H3('EXPLORATORY DATA ANALYSIS',style={'marginTop':'4rem','textAlign':'center','color':'#50006e','marginBottom':'5rem'}),
                                html.H4("Section-1",style={'marginTop':'4rem','textAlign':'center'}),
                                dcc.Graph(id='scatter',
                                figure=px.scatter(merged, x='Code',y='Count', color="Count", size='Count', hover_data=['Description'])
                                    ),
                                html.H4("Section-2",style={'textAlign':'center'}),
                                dcc.Graph(id='scatter2',
                                figure=px.scatter(merged2, x='Code',y='Count',color="Count", size='Count', hover_data=['Description'])
                                    )
                            ]
                        )                                                                                  
                    ),
                    dbc.Col(
                    table,
                    width={"size": 4}
                    ) 
                ]
        )
    ]
)

