import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table

import pandas as pd

import base64
import datetime
import io




app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}



CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("RFM Analysis", className="display-5"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Model", href="/model", id="page-1"),
                dbc.NavLink("Recency", href="/recency", id="page-2"),
                dbc.NavLink("Frequency", href="/frequency", id="page-3"),
                dbc.NavLink("Monetary", href="/monetary", id="page-4"),
                dbc.NavLink("Combo", href="/combo", id="page-5"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)



page_model = html.Div([
    dbc.Row([
        dbc.Col(    
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                multiple=False
            ),width=5
        ),


    ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Label("Column"),width=3),
                dbc.Col(dbc.Label("Analyze"),width=3),
                dbc.Col(dbc.Label("Cluster"),id = "K-cluster-label",width=3),
                dbc.Tooltip(
                    f"Count of Clusters, for self-optimization pass",
                    target=f"K-cluster-label",
                    placement="top")

            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Recency"),width=4),
                        dbc.Checklist(options=[
                        {"label": "", "value": 1},],
                            value=[],
                            id="switches-inline-input",
                            inline=True,
                            switch=True,),
                dbc.Col(dbc.Input(type="number", min=1, max=100, step=1),width=3),
                
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Frequency"),width=4),
                        dbc.Checklist(options=[
                        {"label": "", "value": 2},
                            ],
                            value=[],
                            id="switches-inline-input",
                            inline=True,
                            switch=True,),
                dbc.Col(dbc.Input(type="number", min=1, max=100, step=1),width=3),
                                
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Monatery"),width=4),
                        dbc.Checklist(options=[
                        {"label": "", "value": 3},
                        ],
                        value=[],
                        id="switches-inline-input",
                        inline=True,
                        switch=True,),
                dbc.Col(dbc.Input(type="number", min=1, max=100, step=1),width=3),
                
                
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("All"),width=4),
                        dbc.Checklist(options=[
                        {"label": "", "value": 4},
                        ],
                        value=[],
                        id="switches-inline-input",
                        inline=True,
                        switch=True,),
                dbc.Col(dbc.Input(type="number", min=1, max=100, step=1),width=3),
               
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Text5"),width=4),
                        dbc.Checklist(options=[
                        {"label": "", "value": 5},
                        ],
                        value=[],
                        id="switches-inline-input",
                        inline=True,
                        switch=True,),
                dbc.Col(dbc.Input(type="number", min=1, max=100, step=1),width=3),
               
            ]),
        ],width=3),

    dbc.Row(dbc.Button("Analyze", color="primary", className="mr-1")),

    ]),

    html.Div(id='output-data-upload'),
])


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        html.Hr(), 
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=100
        ),
        html.Hr(),    
    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(content, name, date):
    if content is not None:
        
        children = [
            parse_contents(content, name, date)]
        return children

page_recency = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.P("This is column 1"),
                    width=8,
                    style={"height": "100%", "background-color": "red"},
                ),
                dbc.Col(
                    html.P("This is column 2"),
                    width=4,
                    style={"height": "100%", "background-color": "green"},
                ),
            ],
            className="h-75",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.P("This is column 3"),
                    width=8,
                    style={"height": "100%", "background-color": "blue"},
                ),
                dbc.Col(
                    html.P("This is column 4"),
                    width=4,
                    style={"height": "100%", "background-color": "cyan"},
                ),
            ],
            className="h-25",
        ),
    ],
    style={"height": "100vh"},
)

page_frequency = html.P("This is the content of frewq!")
page_monetary = html.P("This is the content of mone!")
page_combo= html.P("This is the content of combo!")


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(
    [Output(f"page-{i}", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 6)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/model"]:
        return page_model
    elif pathname == "/recency":
        return page_recency
    elif pathname == "/frequency":
        return page_frequency
    elif pathname == "/monetary":
        return page_monetary
    elif pathname == "/combo":
        return page_combo    

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The path {pathname} was not found."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)