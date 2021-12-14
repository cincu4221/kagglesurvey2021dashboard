# html
html.Div(
    children=[
        contents
    ]
)


# bar chart
                    dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "lines",
                                    "hovertemplate": "$%{y:.0f}"
                                    "<extra></extra>"
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "아보카도 평균가격($)",
                                    "x": 2,
                                    "xanchor": "center",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "ticksuffix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    )