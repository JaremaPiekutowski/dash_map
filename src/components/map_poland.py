import json
import plotly.graph_objects as go
# Import Dash elements
import pandas as pd
from dash import Dash, dcc, html
# Import input, output so we can create a callback
from dash.dependencies import Input, Output
# Import all ids
from src.components import ids
# Import DataSchema
from src.data.loader import DataSchema

# Get voivodships
wojewodztwa = json.load(open("src/data/wojewodztwa-medium.geojson"))


# Define a function for rendering the Map
def render(app: Dash, data: pd.DataFrame) -> html.Div:
    # Create a callback function for updating the Map with the variable from dropdown
    @app.callback(
        Output(ids.MAP_POLAND, "children"),
        Input(ids.DROPDOWN, "value"),
    )
    def update_map(variable: str) -> html.Div:
        # filter data for year from the dropdown
        filtered_data = data[[DataSchema.ID, DataSchema.REGION, variable]]
        # show message if no data selected
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")

        # Create our map with selected variable
        fig = go.Figure(data=go.Choropleth(geojson=wojewodztwa,
                                           locations=filtered_data[DataSchema.ID]-1,
                                           z=filtered_data[variable].astype(int),
                                           hovertemplate='%{text}<extra></extra>',
                                           text=filtered_data[variable],
                                           showlegend=False))
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(geo_scope="europe", title=variable, height=750, width=750)

        # Return the updated bar chart
        return html.Div(dcc.Graph(figure=fig), id=ids.MAP_POLAND)

    # Return a Div with the barchart
    return html.Div(id=ids.MAP_POLAND)
