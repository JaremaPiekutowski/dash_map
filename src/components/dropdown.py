# CREATE A DROPDOWN FOR CHOOSING A VARIABLE

# Import Dash class, html as well as "dcc" which is a library of UI components
import pandas as pd
from dash import Dash, html, dcc
# Import *ids* FROM ids.py file in components - TODO:Necessary?
from src.components import ids


# Create a function to return a div with our Dropdown allowing us to choose a Variable
def render(app: Dash, data: pd.DataFrame) -> html.Div:
    variables: list[str] = data.columns[2:].tolist()
    # Return the div with the dropdown
    return html.Div(
        # Define the div's children
        children=[
            # Heading 6 showing the dropdown title
            html.H6("Wskaźnik"),
            # Add dropdown component
            dcc.Dropdown(
                # Set ID
                id=ids.DROPDOWN,
                # Define dropdown options
                options=[{"label": variable, "value": variable} for variable in variables],
                # Set initial value
                value=variables[0],
                # Allow multiple choice
                multi=False
            )
        ]
    )
