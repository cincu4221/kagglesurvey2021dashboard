import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("data/kaggle_survey_2021_responses.csv", index_col=0)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
app.title = "2021 kaggle survey"
server = app.server

def dropdown():
    sel_dropdown = dcc.Dropdown(
        id=DD_id,
        options={
            {"label": }
        }
    )

def graph(graph_type):
    chart = dcc.Graph(
        figure={
            "data": [
                {
                    "x":
                    "y":
                    "type": graph_type,
                },
            ],
        },
    )
    return chart


# ---- html ----
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="📈", className="header_emoji"),
                html.H1(children="2021 Kaggle Machine Learning & Data Science Survey", className="header_title"),
                html.P(children="My Notebook submitted to kaggle", className="header_description")
            ],
            className='header'
        ),
        html.Div(
            children=[
                graph()
            ],
            className="card"
        )
    ]
)




if __name__ == "__main__":
    app.run_server(debug=True)