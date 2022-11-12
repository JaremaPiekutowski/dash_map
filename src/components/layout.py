# CREATE A LAYOUT FOR OUR APP

# Import Dash and html
import pandas as pd
from dash import Dash, html
# Import dropdown for years
from src.components import dropdown, map_poland


# A function for creating layout (inside a div)
def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    # Return a div which will be our layout
    return html.Div(
        # Define class name of the div
        className="app-div",
        # Define children of the div
        children=[
            # This H1 will display the title of the app
            html.H1(app.title),
            # Horizontal line
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    dropdown.render(app, data),
                ]
            ),
            map_poland.render(app, data)
        ]
    )
