import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

# step 1. Data Import
data = pd.read_csv("data/kaggle_survey_2021_responses.csv", index_col=0)
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

@app.callback(
    [Output("price-chart", "figure"), Output("volume-chart", "figure")],
    [
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(region, avocado_type, start_date, end_date):
    mask = (
        (data.region == region)
        & (data.type == avocado_type)
        & (data.Date >= start_date)
        & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
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

# step 3. HTML
app.layout = html.Div(
    # Header Message
    children=[
        html.Div(
            children=[
                html.P(children="📈", className="header_emoji"),
                html.H1(children="temp Analytics", className="header_title"),
                html.P(children="Temp", className="header_description")
            ],
            className='header'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Age", className="menu-title"),
                        dcc.Dropdown(
                            id="age-filter",
                            options=[
                                {"label": age, "value": Q1}
                                for age in np.sort(data.Q1[1:].unique())
                            ],
                            value="18-21",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Gender", className="menu-title"),
                        dcc.Dropdown(
                            id="Gender-filter",
                            options=[
                                {"label": gender, "value": Q2}
                                for gender in data.Q2[1:].unique()
                            ],
                            value="Man",
                            clearable=False,
                            searchable=False,
                            className="dropdown"
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(children="Country", className="menu-title"),
                        dcc.Dropdown(
                            id="Country-filter",
                            options=[
                                {"label": country, "value": Q3}
                                for country in data.Q3[1:].unique()
                            ],
                            value="India",
                            clearable=False,
                            searchable=False,
                            className="dropdown"
                        ),
                    ],
                ),
            ],
            className="menu",
        ),

    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
