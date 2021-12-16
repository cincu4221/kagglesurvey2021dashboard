import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Output, Input

# step 1. Data Import
data = pd.read_csv("data/kaggle_survey_2021_responses.csv", index_col=0)
Age_xaxis = data[data['Q3'] == 'Japan']['Q1'].value_counts().sort_index().index
Age_yaxis = data[data['Q3'] == 'Japan']['Q1'].value_counts().sort_index().values
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
# data.sort_values("Date", inplace=True)

# print(data[['region', 'type', 'Date']].head())

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

colors = {
    'background': '#111827',
    'content-background': '#1B263D',
    'plot_background': '#324773',
    'text': '#d3d3d3'
}
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
# Chart.1
fig_age = go.Figure(data=[go.Bar(x=data['Q1'][1:].value_counts().sort_index().index,
                                 y=data['Q1'][1:].value_counts().sort_index().values,
                                 )])

fig_age.update_traces(hovertemplate='(Count: %{y:.0f})',
                      marker_color='aqua')
fig_age.update_layout(paper_bgcolor=colors['content-background'],
                      font_color=colors['text'],
                      plot_bgcolor=colors['plot_background'],
                      autosize=True)

# Chart.2
fig_gender = go.Figure(data=[go.Pie(labels=data['Q2'][1:].value_counts().sort_index().index,
                                    values=data['Q2'][1:].value_counts().sort_index().values,
                                    textinfo='label+percent',
                                    hole=.3)])
fig_gender.update_layout(paper_bgcolor=colors['content-background'],
                         font_color=colors['text'],
                         showlegend=False,
                         autosize=True)

# Chart.3

# step 3. HTML
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Button(className='Red-btn'),
                html.Button(className='Yellow-btn'),
                html.Button(className='Green-btn'),
            ],
            className='Top-bar'
        ),
        html.Div(
            children=[
                html.P(children="📈", className="header_emoji"),
                html.H1(children="2021 Kaggle Machine Learning & Data Science Survey", className="header_title"),
                html.P(children="My Notebook submitted to kaggle", className="header_description")
            ],
            className='header'
        ),
        dcc.Tabs([
            dcc.Tab(
                label='Dashboard', children=[
                    html.Div(
                        children=[
                            html.H1(style={'color': colors['text']},
                                    children="Dashboard"
                            ),
                            html.Div(
                                children=[
                                    html.Div(children=[
                                        html.P("Age Distribution",className='sub_title')
                                    ]),
                                    html.Div(dcc.Graph(figure=fig_age,
                                                       style={'margin': 5}),className='under_radius')
                                ],
                                className='section_age'
                            ),
                            html.Div(
                                children=[
                                    html.Div(children=[
                                        html.P("Gender Distribution", className='sub_title')
                                    ]),
                                    html.Div(dcc.Graph(figure=fig_gender,
                                                       style={'margin': 5}), className='under_radius')
                                ],
                                className='section_gen'
                            ),
                            html.Div(
                                children=[
                                    dcc.Graph(figure=fig_age)
                                ],
                                className='section_age'
                            ),
                            html.Div(
                                style={'backgroundColor': colors['content-background']},
                                children=[
                                    html.P(children="SECTION 영역",
                                           style={'color': colors['text']})
                                ],
                                className='section'
                            ),
                        ],className='BGC-navy'
                    ),
                ],
            ),
            dcc.Tab(
                label='Introduce', children=[
                    dcc.Graph(
                        id="Age-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data[data['Q3'] == 'Japan']['Q1'].value_counts().sort_index().index,
                                    "y": data[data['Q3'] == 'Japan']['Q1'].value_counts().sort_index().values,
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
                    ),
                    html.P(children="test text")
                ]
            ),
            dcc.Tab(
                label='HTML layout Exam', children=[
                    html.H1(children="HTML5 레이아웃"),
                    html.Header(
                        children=[
                            html.H2(children="HEADER 영역")
                        ],
                        className='header_test'
                    ),
                    html.Nav(
                        children=[
                            html.H2(children="NAV 영역")
                        ],
                        className='nav'
                    ),
                    html.Section(
                        children=[
                            html.P(children="SECTION 영역")
                        ],
                        className='section'
                    ),
                    html.Footer(
                        children=[
                            html.H2(children="FOOTER 영역")
                        ],
                        className='footer'
                    )
                ],
            ),
        ], className='Tabs-cover')
    ], className='Page-cover'
)

if __name__ == "__main__":
    app.run_server(debug=True)
