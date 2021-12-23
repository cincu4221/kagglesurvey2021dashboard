import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("data/kaggle_survey_2021_responses.csv", index_col=0)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


# Tab_CSS
Tab_deco = {
    'background-color': '#1B263D',
    'color': 'lightgrey',
    'border': '1px solid #1B263D',
    'margin': '5px',
    'border-radius': '10px 10px 0 0',
}

sel_Tab_deco = {
    'background-color': '#324773',
    'color': 'lightgrey',
    'border': 'none',
    'margin': '5px',
    'border-bottom': '5px solid',
    'border-radius': '10px 10px 0 0'
}

Data_Tab = {
    'color': 'lightgrey',
    'background-color': '#1B263D',
    'border-radius': '10px 10px 0 0',
    'border': 'none'
}

Data_Tab_selected = {
    'background-color': '#BAD9D6',
    'border-radius': '10px 10px 0 0',
    'border': 'none'
}

data_pivot = [['Age', 'Gender', 'Country', 'Job', 'Career']]
for num in list(range(25973)):
    data_pivot.append([
        data['Q1'][1:].values[num],
        data['Q2'][1:].values[num],
        data['Q3'][1:].values[num],
        data['Q5'][1:].values[num],
        data['Q6'][1:].values[num]])

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
                        html.H1(children="2021 Kaggle Machine Learning & Data Science Survey",
                                className="header_title"),
                        html.P(children="My Notebook submitted to kaggle", className="header_description")
                    ],
                    className='header'
                ),
                dcc.Tabs([
                    dcc.Tab(
                        label='Visualization', style=Tab_deco, selected_style=sel_Tab_deco,
                        children=[],
                    ),
                    dcc.Tab(
                        label='PivotTable', style=Tab_deco, selected_style=sel_Tab_deco, children=[]
                    ),
                    dcc.Tab(
                        label='Data & Description', style=Tab_deco, selected_style=sel_Tab_deco, children=[],
                    ),
                ], className='Tabs-cover')
            ], className='Dash-cover'
        )
    ], className='Page-cover'
)


if __name__ == '__main__':
    app.run_server(debug=True)