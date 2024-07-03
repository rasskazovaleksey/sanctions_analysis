import pandas as pd 
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.read_csv('data/heart_statlog_cleveland_hungary_final.csv')

app.layout = [
    html.Div(children='Heart Disease Dataset'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    html.Hr(),
    html.Div(children='Distribution of attributes'),
    dcc.Dropdown(options=df.columns, value=df.columns[0], id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph'),
    html.Div(children='Correlation Matrix'),
    dcc.Graph(figure={}, id='corr_matrix'),
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df[col_chosen], x=col_chosen)
    return fig

if __name__ == '__main__':
    app.run(debug=True)

