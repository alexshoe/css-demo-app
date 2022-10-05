import dash
from dash import dcc, html, dash_table, Input, Output, State
import dash_mantine_components as dmc
import plotly.express as px


def sidebar():
    return html.Div(
        dmc.Center("Filters hehe 😰"),
        className="app-sidebar card",
        style={"background-image": "linear-gradient(rgb(0, 214, 186), rgb(0, 0, 160))"},
    )


def chunk_of_cards():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        style={"width": "500px", "height": "400px"},
                        className="card",
                    ),
                    html.Div(
                        style={"width": "500px", "height": "400px"},
                        className="card",
                    ),
                ],
                className="flex-row",
            ),
            html.Div(
                html.Div(
                    style={"width": "1000px", "height": "400px"},
                    className="card",
                ),
                className="flex-row",
            ),
            html.Div(
                html.Div(
                    style={"width": "1000px", "height": "400px"},
                    className="card",
                ),
                className="flex-row",
            ),
            html.Div(
                html.Div(
                    style={"width": "1000px", "height": "400px"},
                    className="card",
                ),
                className="flex-row",
            ),
        ],
        style={"height": "calc(100vh - 100px)", "overflow-y": "scroll"},
    )


def layout():
    return html.Div(
        [
            sidebar(),
            chunk_of_cards(),
        ],
        className="flex-row",
    )
