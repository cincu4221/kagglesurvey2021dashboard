import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="📈", className="header_emoji"),
                html.H1(children="temp Analytics", className="header_title"),
                html.P(children="Temp", className="header_description")
            ],
            className='header'
        ),
    ]
)

@app.callback(dash.dependencies.Output('display-value', 'children'),
                [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)

server.secret_key = os.environ.get(‘SECRET_KEY’, ‘my-secret-key’)