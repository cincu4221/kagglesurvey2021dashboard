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

@app.callback(
    [Output("Age-chart", "figure"), Output("gender-chart", "figure"), Output("Country-chart", "figure")],
    [
        Input("age-filter", "value"),
        Input("type-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(age, gender, country, start_date, end_date):
    mask = (
        (data.Q1 == age)
        & (data.Q2 == gender)
        & (data.Q3 == country)
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
                                {"label": age, "value": age}
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
                                {"label": gender, "value": gender}
                                for gender in np.sort(data.Q2[1:].unique())
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
                                {"label": country, "value": country}
                                for country in np.sort(data.Q3[1:].unique())
                            ],
                            value="Algeria",
                            clearable=False,
                            searchable=False,
                            className="dropdown"
                        ),
                    ],
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="Age-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": Age_xaxis,
                                    "y": Age_yaxis,
                                    "type": "bar",
                                    "hovertemplate": "$%{y:.2f}"
                                    "<extra></extra>"
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "국가별 캐글러 나이 분포",
                                    "x": 2,
                                    "xanchor": "center",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                    ),

                ],
                className="wrapper"
            ),
        ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
