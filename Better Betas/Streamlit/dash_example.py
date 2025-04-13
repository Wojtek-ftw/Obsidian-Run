from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv("data.csv")

app.layout = html.Div([
    dcc.Dropdown(df.columns, id='col'),
    dcc.Graph(id='plot')
])

@app.callback(
    Output('plot', 'figure'),
    Input('col', 'value')
)
def update_plot(col):
    return px.line(df, y=col)

app.run_server(debug=True)
