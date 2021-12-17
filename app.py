import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
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

# Chart.1
def age_chart_func(country):
    fig_age = px.bar(data,
                     x=data[data['Q3'] == country]['Q1'][1:].value_counts().sort_index().index,
                     y=data[data['Q3'] == country]['Q1'][1:].value_counts().sort_index().values,)
    fig_age.update_traces(hovertemplate='(Count: %{y:.0f})',
                          marker_color='lightgreen')
    fig_age.update_layout(paper_bgcolor=colors['content-background'],
                          font_color=colors['text'],
                          plot_bgcolor=colors['plot_background'],
                          autosize=True)
    fig_age.update_xaxes(title_text='Age Distribution')
    fig_age.update_yaxes(title_text='Counts')
    return fig_age


''' Graph_object style
fig_age = go.Figure(data=[go.Bar(x=data['Q1'][1:].value_counts().sort_index().index,
                                 y=data['Q1'][1:].value_counts().sort_index().values,
                                 )])

fig_age.update_traces(hovertemplate='(Count: %{y:.0f})',
                      marker_color='lightgreen')
fig_age.update_layout(paper_bgcolor=colors['content-background'],
                      font_color=colors['text'],
                      plot_bgcolor=colors['plot_background'],
                      autosize=True)
'''

# Chart.2
fig_gender = px.pie(data,
                    names=data['Q2'][1:].value_counts().sort_index().index,
                    values=data['Q2'][1:].value_counts().sort_index().values,
                    hole=.3
                    )
fig_gender.update_traces(textinfo='label+percent')
fig_gender.update_layout(paper_bgcolor=colors['content-background'],
                         font_color=colors['text'],
                         showlegend=True,
                         autosize=True)

''' Graph_object style
fig_gender = go.Figure(data=[go.Pie(labels=data['Q2'][1:].value_counts().sort_index().index,
                                    values=data['Q2'][1:].value_counts().sort_index().values,
                                    textinfo='label+percent',
                                    hole=.3)])
fig_gender.update_layout(paper_bgcolor=colors['content-background'],
                         font_color=colors['text'],
                         showlegend=False,
                         autosize=True)
'''

# Chart.3


# Tab_CSS
Tab_deco = {
    'background-color': '#1B263D',
    'color': 'lightgrey',
    'border': '1px solid #1B263D',
    'margin': '5px',
    'border-radius': '10px 10px 0 0'
}

sel_Tab_deco = {
    'background-color': '#324773',
    'color': 'lightgrey',
    'border': 'none',
    'margin': '5px',
    'border-bottom': '5px solid',
    'border-radius': '10px 10px 0 0'
}

# step 3. HTML
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Button(className='Red-btn'),
                        html.Button(className='Yellow-btn'),
                        html.Button(className='Green-btn'),
                        html.Div(
                            className='Div_center',
                            children=[
                                html.P(
                                    children="2021 Kaggle Machine Learning & Data Science Survey.dashboard",
                                    className="Top_bar_title"
                                )
                            ]
                        )
                    ],
                    className='Top_bar'
                ),
                html.Div(
                    children=[
                        html.H1(children="2021 Kaggle Machine Learning & Data Science Survey", className="header_title"),
                        html.P(children="My Notebook submitted to kaggle", className="header_description")
                    ],
                    className='header'
                ),
                dcc.Tabs([
                    dcc.Tab(
                        label='Dashboard', style=Tab_deco, selected_style=sel_Tab_deco,
                        children=[
                            html.Div(
                                children=[
                                    html.Div(
                                        children=[
                                            html.H1(
                                                style={'color': colors['text'],
                                                       'margin': '1%'},
                                                children="Filter Area"
                                            ),
                                        ]
                                    ),
                                    html.Div(
                                        children=[
                                            html.Div(children=[
                                                html.P("Age Distribution",className='sub_title')
                                            ]),
                                            dcc.Dropdown(
                                                id="country-filter",
                                                options=[
                                                    {"label": country, "value": country}
                                                    for country in np.sort(data.Q3[1:].unique())
                                                ],
                                                value="Algeria",
                                            ),
                                            html.Div(dcc.Graph(figure=age_chart_func('Algeria'),
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
                                            html.Div(children=[
                                                html.P("Country Distribution", className='sub_title')
                                            ]),
                                            html.Div(dcc.Graph(figure=age_chart_func('Algeria'),
                                                               style={'margin': 5}), className='under_radius')
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
                                ],className='contents-padding'
                            ),
                        ],
                    ),
                    dcc.Tab(
                        label='Introduce', style=Tab_deco, selected_style=sel_Tab_deco, children=[
                            html.H2('Hello World'),
                            dcc.Dropdown(
                                id='dropdown',
                                options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
                                value='LA'
                            ),
                            html.Div(id='display-value')
                        ]
                    ),
                    dcc.Tab(
                        label='HTML layout Exam', style=Tab_deco, selected_style=sel_Tab_deco, children=[
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
            ],className='Dash-cover'
        )
    ],className='Page-cover'
)

@app.callback(
    Output('', 'children'),
    Input('country-filter', 'value'))
def age_chart_func(value):
    return 'You have selected "{}"'.format(value)

# test
@app.callback(
    Output('display-value', 'children'),
    Input('dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.run_server(debug=True)
