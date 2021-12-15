import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

# step 1. Data Import
data = pd.read_csv("data/kaggle_survey_2021_responses.csv", index_col=0)
Age_xaxis = data[data['Q3'] == 'Japan']['Q1'].value_counts().sort_index().index
Age_yaxis = data[data['Q3'] == 'Japan']['Q1'].value_counts().sort_index().values
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
# data.sort_values("Date", inplace=True)

#print(data[['region', 'type', 'Date']].head())

# step 2. Dash Class
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Temp Analytics: Understand Your Data!"
server = app.server
"""
@app.callback(
    [Output("Age-chart", "figure"), Output("Gender-chart", "figure"), Output("Country-chart", "figure")],
    [
        Input("age-filter", "value"),
        Input("gender-filter", "value"),
        Input("country-filter", "value"),
    ],
)
def update_charts(age, gender, country ):
    mask = (
        (data.Q1 == age)
        & (data.Q2 == gender)
        & (data.Q3 == country)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}명<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {
                "text": "Avocados Sold",
                "x": 0.05,
                "xanchor": "left"
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure

"""
# step 3. HTML
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
        dcc.Tabs([
            dcc.Tab(label='Tab one', children=[
                dcc.Graph(
                    id="Age-chart",
                    config={"displayModeBar": False},
                    figure={
                        "data": [
                            {
                                "x": Age_xaxis,
                                "y": Age_yaxis,
                                "type": "bar",
                                "hovertemplate": "(Count : %{y:.0f})"
                                                 "<extra></extra>"
                            },
                        ],
                        "layout": {
                            "title": {
                                "text": "Age",
                                "x": 2,
                                "xanchor": "center",
                            },
                            "xaxis": {"fixedrange": True},
                            "yaxis": {
                                "tickprefix": "",  # y축 단위
                                "fixedrange": True,
                            },
                            "colorway": ["#17B897"],
                        },
                    }
                )
            ]),
            dcc.Tab(label='Tab two', children=[
                dcc.Graph(
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [1, 4, 1],
                             'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [1, 2, 3],
                             'type': 'bar', 'name': u'Montréal'},
                        ]
                    }
                )
            ]),
            dcc.Tab(label='Tab three', children=[
                dcc.Graph(
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [2, 4, 3],
                             'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [5, 4, 3],
                             'type': 'bar', 'name': u'Montréal'},
                        ]
                    }
                ),
            ]),
        ])
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
