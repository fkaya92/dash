import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])



app.layout = html.Div([

    dbc.Row(dbc.Col(html.Div("A single column"))),
            
    dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]),


    dbc.Row(dbc.Col(html.Div("A single, half-width column"), width=6)),
    dbc.Row(
        dbc.Col(html.Div("An automatically sized column"), width="auto")
    ),
    dbc.Row(
        [
            dbc.Col(html.Div("One of three columns"), width=3),
            dbc.Col(html.Div("One of three columns")),
            dbc.Col(html.Div("One of three columns"), width=3),
        ]
    ),

    dbc.Alert("This is a primary alert", color="primary"),
    dbc.Alert("This is a secondary alert", color="secondary"),
    dbc.Alert("This is a success alert! Well done!", color="success"),
    dbc.Alert("This is a warning alert... be careful...", color="warning"),
    dbc.Alert("This is a danger alert. Scary!", color="danger"),
    dbc.Alert("This is an info alert. Good to know!", color="info"),
    dbc.Alert("This is a light alert", color="light"),
    dbc.Alert("This is a dark alert", color="dark"),



])



if __name__ == '__main__':
    app.run_server(debug=True)