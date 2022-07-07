import pandas as pd
import dask.dataframe as dd
from dash import html , dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


register_page(__name__, path="/eda")



features = pd.read_excel('gs://lidar-data-01/datasets/featureCodes.xlsx')
features = features.sort_values(['Feature Code'], ascending=True).reset_index(drop=True)
features.columns = ["Code", "Description"]
features.reset_index().rename(columns={'index': ''})
table = dbc.Table.from_dataframe(
    features, striped=True, bordered=True, hover=True, index=False
)

lista = ["Trees greater than 1m in height","Natural ground","Trees less than 1m in height","MDT Ground","Low Vegetation Risk"]

# df_dd = dd.read_csv('gs://lidar-data-01/datasets/MDS-01.csv')
# df = df_dd.compute()
# code_data = pd.DataFrame(df["Code"].value_counts()).reset_index()
# code_data.columns = ["Code", "Count"]
# merged = pd.merge(code_data, features, on="Code")

# df_dd2 = dd.read_csv('gs://lidar-data-01/datasets/MDS-02.csv')
# df2 = df_dd2.compute()
# code_data2 = pd.DataFrame(df2["Code"].value_counts()).reset_index()
# code_data2.columns = ["Code", "Count"]
# merged2 = pd.merge(code_data2, features, on="Code")

df = pd.read_csv('gs://lidar-data-01/datasets/count_table.csv')
table2 = dbc.Table.from_dataframe(
    df, striped=True, bordered=True, hover=True, index=False
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                

                dbc.Col(
                    html.Div(
                            [
                                html.H4('EXPLORATORY DATA ANALYSIS',style={'marginTop':'4rem','textAlign':'center','color':'#50006e','marginBottom':'5rem'}),
                                html.H5("Feature code count",style={'marginTop':'4rem','textAlign':'left'}),
                                html.Br(),
                                html.P("Along the Toledo - Zamore transmission line there are more than 60 million points dstributed \
                                    as follows:"),
                                dcc.Graph(id='scatter',
                                figure=px.scatter(df, x='Code',y='Count', color="Count", size='Count', hover_data=['Description'])
                                    ),#,
                                html.P("According to the metada file that ISA provided, there are 35 categories or codes to identify \
                                    objects and risks based on the position of each data point but only 20 of those codes are\
                                    present on the whole data-set."),
                                html.P("Most common object types found in the dataset are:"),
                                html.Ol([html.Li(x) for x in lista])

                                # html.H4("Section-2",style={'textAlign':'center'}),
                                # dcc.Graph(id='scatter2',
                                # figure=px.scatter(merged2, x='Code',y='Count',color="Count", size='Count', hover_data=['Description'])
                                #     )
                            ]
                        )                                                                                  
                    ),
                    dbc.Col(
                    table2,
                    width={"size": 4}
                    ) 
                ]
        )
    ]
)

