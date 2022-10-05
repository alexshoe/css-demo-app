import dash
from dash import dcc, html, dash_table, Input, Output, State
import dash_mantine_components as dmc
import plotly.express as px

import pages


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
)

app.title = "CSS Demo App"
server = app.server


def generate_header():
    return html.Div(
        [
            html.H1("Mommy and Daddy's Pee Pee App"),
            html.Div(
                [
                    dcc.Link(href=app.get_relative_path("/"), children="Home 🍼"),
                    dmc.Space(w=20),
                    dcc.Link(
                        href=app.get_relative_path("/other_page"),
                        children="Other Page 🐌",
                    ),
                ],
                className="flex-row",
                # style={"margin-left": "auto"},
            ),
        ],
        className="flex-row",
        style={
            "background-color": "white",
            # "border": "1px solid #cacaca",
            "border-radius": "10px",
            "width": "100%vw",
            "padding": "10px",
            "margin": "0px 20px",
            "height": "50px",
            "align-items": "center",
            "display": "flex",
            "justify-content": "space-between",
        },
    )


app.layout = html.Div(
    [
        html.Link(
            href="https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;400;700&display=swap"
        ),
        generate_header(),
        dcc.Location(id="url"),
        html.Div(id="content"),
    ],
)


@app.callback(
    Output("content", "children"),
    Input("url", "pathname"),
)
def display_content(pathname):
    page_name = app.strip_relative_path(pathname)

    if not page_name:  # None or ''
        return pages.home.layout()
    elif page_name == "other_page":
        return pages.other_page.layout()

    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
